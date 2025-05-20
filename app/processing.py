from datetime import datetime

def get_setting(db, key, default):
    result = db.fetchone("SELECT value FROM Settings WHERE key = ?", (key,))
    return result[0] if result else default

def create_import_receipt(db, receipt_data):
    min_import_qty = int(get_setting(db, 'min_import_quantity', '150'))
    max_stock_for_import = int(get_setting(db, 'max_stock_for_import', '300'))
    
    for item in receipt_data['items']:
        book_id = item['book_id']
        quantity = item['quantity']
        stock = db.fetchone("SELECT stock FROM Books WHERE book_id = ?", (book_id,))[0]
        if stock >= max_stock_for_import:
            raise ValueError(f"Sách với mã {book_id} có tồn kho {stock} >= {max_stock_for_import}")
        if quantity < min_import_qty:
            raise ValueError(f"Số lượng nhập {quantity} < {min_import_qty}")
    
    db.execute("INSERT INTO Import_Receipts (date) VALUES (?)", (receipt_data['date'],))
    receipt_id = db.cursor.lastrowid
    
    for item in receipt_data['items']:
        db.execute("INSERT INTO Import_Receipt_Details (receipt_id, book_id, quantity, import_unit_price) VALUES (?, ?, ?, ?)",
                   (receipt_id, item['book_id'], item['quantity'], item['import_unit_price']))
        db.execute("UPDATE Books SET stock = stock + ?, import_unit_price = ? WHERE book_id = ?",
                   (item['quantity'], item['import_unit_price'], item['book_id']))
    
    db.conn.commit()

def create_sales_invoice(db, invoice_data):
    max_debt = float(get_setting(db, 'max_debt_for_sale', '20000'))
    min_stock_after_sale = int(get_setting(db, 'min_stock_after_sale', '20'))
    
    customer_id = invoice_data['customer_id']
    debt = db.fetchone("SELECT debt FROM Customers WHERE customer_id = ?", (customer_id,))[0]
    if debt > max_debt:
        raise ValueError(f"Khách hàng có nợ {debt} vượt quá giới hạn {max_debt}")
    
    total_amount = 0
    for item in invoice_data['items']:
        book_id = item['book_id']
        quantity = item['quantity']
        stock = db.fetchone("SELECT stock, import_unit_price FROM Books WHERE book_id = ?", (book_id,))
        if stock[0] < quantity + min_stock_after_sale:
            raise ValueError(f"Sách {item['name']} có tồn kho {stock[0]} không đủ để bán")
        selling_price = stock[1] * 1.05  # Giá bán = 105% giá nhập
        total_amount += quantity * selling_price
        item['selling_unit_price'] = selling_price
    
    remaining_amount = total_amount - invoice_data['amount_paid']
    if remaining_amount < 0:
        raise ValueError("Số tiền trả vượt quá tổng tiền")
    
    db.execute("INSERT INTO Sales_Invoices (date, customer_id, total_amount, amount_paid, remaining_amount) VALUES (?, ?, ?, ?, ?)",
               (invoice_data['date'], customer_id, total_amount, invoice_data['amount_paid'], remaining_amount))
    invoice_id = db.cursor.lastrowid
    
    for item in invoice_data['items']:
        db.execute("INSERT INTO Sales_Invoice_Details (invoice_id, book_id, quantity, selling_unit_price) VALUES (?, ?, ?, ?)",
                   (invoice_id, item['book_id'], item['quantity'], item['selling_unit_price']))
        db.execute("UPDATE Books SET stock = stock - ? WHERE book_id = ?",
                   (item['quantity'], item['book_id']))
    
    db.execute("UPDATE Customers SET debt = debt + ? WHERE customer_id = ?",
               (remaining_amount, customer_id))
    
    db.conn.commit()

def create_payment_receipt(db, receipt_data):
    restrict_payment = get_setting(db, 'restrict_payment', 'True') == 'True'
    customer_id = receipt_data['customer_id']
    amount = receipt_data['amount_collected']
    
    if restrict_payment:
        debt = db.fetchone("SELECT debt FROM Customers WHERE customer_id = ?", (customer_id,))[0]
        if amount > debt:
            raise ValueError(f"Số tiền thu {amount} vượt quá nợ {debt}")
    
    db.execute("INSERT INTO Payment_Receipts (date, customer_id, amount_collected) VALUES (?, ?, ?)",
               (receipt_data['date'], customer_id, amount))
    db.execute("UPDATE Customers SET debt = debt - ? WHERE customer_id = ?",
               (amount, customer_id))
    
    db.conn.commit()

def get_inventory_report(db, year, month):
    start_date = datetime(year, month, 1).strftime('%Y-%m-%d')
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1
    end_date = datetime(next_year, next_month, 1).strftime('%Y-%m-%d')
    
    books = db.fetchall("SELECT book_id, name FROM Books")
    report = []
    
    for book in books:
        book_id, name = book
        imports_before = db.fetchone("""
            SELECT SUM(quantity)
            FROM Import_Receipt_Details d
            JOIN Import_Receipts r ON d.receipt_id = r.receipt_id
            WHERE d.book_id = ? AND r.date < ?
        """, (book_id, start_date))[0] or 0
        sales_before = db.fetchone("""
            SELECT SUM(quantity)
            FROM Sales_Invoice_Details d
            JOIN Sales_Invoices i ON d.invoice_id = i.invoice_id
            WHERE d.book_id = ? AND i.date < ?
        """, (book_id, start_date))[0] or 0
        beginning_stock = imports_before - sales_before
        
        imports_during = db.fetchone("""
            SELECT SUM(quantity)
            FROM Import_Receipt_Details d
            JOIN Import_Receipts r ON d.receipt_id = r.receipt_id
            WHERE d.book_id = ? AND r.date >= ? AND r.date < ?
        """, (book_id, start_date, end_date))[0] or 0
        sales_during = db.fetchone("""
            SELECT SUM(quantity)
            FROM Sales_Invoice_Details d
            JOIN Sales_Invoices i ON d.invoice_id = i.invoice_id
            WHERE d.book_id = ? AND i.date >= ? AND i.date < ?
        """, (book_id, start_date, end_date))[0] or 0
        transactions = imports_during - sales_during
        ending_stock = beginning_stock + transactions
        
        report.append({
            'book_name': name,
            'beginning_stock': beginning_stock,
            'transactions': transactions,
            'ending_stock': ending_stock
        })
    
    return report

def get_debt_report(db, year, month):
    start_date = datetime(year, month, 1).strftime('%Y-%m-%d')
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1
    end_date = datetime(next_year, next_month, 1).strftime('%Y-%m-%d')
    
    customers = db.fetchall("SELECT customer_id, name FROM Customers")
    report = []
    
    for customer in customers:
        customer_id, name = customer
        debt_before = db.fetchone("""
            SELECT SUM(remaining_amount)
            FROM Sales_Invoices
            WHERE customer_id = ? AND date < ?
        """, (customer_id, start_date))[0] or 0
        payments_before = db.fetchone("""
            SELECT SUM(amount_collected)
            FROM Payment_Receipts
            WHERE customer_id = ? AND date < ?
        """, (customer_id, start_date))[0] or 0
        beginning_debt = debt_before - payments_before
        
        debt_during = db.fetchone("""
            SELECT SUM(remaining_amount)
            FROM Sales_Invoices
            WHERE customer_id = ? AND date >= ? AND date < ?
        """, (customer_id, start_date, end_date))[0] or 0
        payments_during = db.fetchone("""
            SELECT SUM(amount_collected)
            FROM Payment_Receipts
            WHERE customer_id = ? AND date >= ? AND date < ?
        """, (customer_id, start_date, end_date))[0] or 0
        transactions = debt_during - payments_during
        ending_debt = beginning_debt + transactions
        
        report.append({
            'customer_name': name,
            'beginning_debt': beginning_debt,
            'transactions': transactions,
            'ending_debt': ending_debt
        })
    
    return report