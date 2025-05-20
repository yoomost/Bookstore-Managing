import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from processing import create_sales_invoice

class SalesInvoiceForm:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        
        # Customer selection
        tk.Label(parent, text='Khách hàng:').grid(row=0, column=0, padx=5, pady=5)
        customers = self.db.fetchall("SELECT customer_id, name FROM Customers")
        self.customer_dict = {c[1]: c[0] for c in customers}
        self.customer_var = tk.StringVar()
        self.customer_combobox = ttk.Combobox(parent, textvariable=self.customer_var, values=list(self.customer_dict.keys()), state='readonly')
        self.customer_combobox.grid(row=0, column=1, padx=5, pady=5)
        
        # Button to add new customer
        tk.Button(parent, text='Thêm khách hàng mới', command=self.add_new_customer).grid(row=0, column=2, padx=5, pady=5)
        
        # Date entry
        tk.Label(parent, text='Ngày lập:').grid(row=1, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(parent)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)
        self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
        
        # Amount paid entry
        tk.Label(parent, text='Số tiền trả:').grid(row=2, column=0, padx=5, pady=5)
        self.amount_paid_entry = tk.Entry(parent)
        self.amount_paid_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Treeview for books
        self.tree = ttk.Treeview(parent, columns=('STT', 'Book ID', 'Name', 'Genre', 'Quantity', 'Selling Price'), show='headings')
        self.tree.heading('STT', text='STT')
        self.tree.heading('Book ID', text='Mã sách')
        self.tree.heading('Name', text='Tên sách')
        self.tree.heading('Genre', text='Thể loại')
        self.tree.heading('Quantity', text='Số lượng')
        self.tree.heading('Selling Price', text='Đơn giá bán')
        self.tree.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
        
        # Buttons
        tk.Button(parent, text='Thêm sách', command=self.add_book).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(parent, text='Xóa sách', command=self.remove_book).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(parent, text='Lưu hóa đơn', command=self.save_invoice).grid(row=5, column=0, columnspan=3, padx=5, pady=5)
    
    def add_new_customer(self):
        dialog = tk.Toplevel(self.parent)
        dialog.title("Thêm khách hàng mới")
        
        # Labels and entries
        tk.Label(dialog, text='Tên:').grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(dialog)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(dialog, text='Địa chỉ:').grid(row=1, column=0, padx=5, pady=5)
        address_entry = tk.Entry(dialog)
        address_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(dialog, text='Điện thoại:').grid(row=2, column=0, padx=5, pady=5)
        phone_entry = tk.Entry(dialog)
        phone_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(dialog, text='Email:').grid(row=3, column=0, padx=5, pady=5)
        email_entry = tk.Entry(dialog)
        email_entry.grid(row=3, column=1, padx=5, pady=5)
        
        def save_new_customer():
            name = name_entry.get()
            address = address_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            if not name:
                messagebox.showerror("Lỗi", "Vui lòng nhập tên khách hàng")
                return
            # Insert into database
            self.db.execute("INSERT INTO Customers (name, address, phone, email, debt) VALUES (?, ?, ?, ?, 0)", 
                           (name, address, phone, email))
            new_id = self.db.cursor.lastrowid
            # Update customer_dict
            self.customer_dict[name] = new_id
            # Update combobox
            self.customer_combobox['values'] = list(self.customer_dict.keys())
            # Select the new customer
            self.customer_var.set(name)
            # Close dialog
            dialog.destroy()
        
        tk.Button(dialog, text='Lưu', command=save_new_customer).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    
    def add_book(self):
        dialog = tk.Toplevel(self.parent)
        tk.Label(dialog, text='Sách:').grid(row=0, column=0, padx=5, pady=5)
        books = self.db.fetchall("SELECT book_id, name, genre, import_unit_price FROM Books")
        self.book_dict = {b[1]: (b[0], b[2], b[3]) for b in books}
        self.book_var = tk.StringVar()
        ttk.Combobox(dialog, textvariable=self.book_var, values=list(self.book_dict.keys()), state='readonly').grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(dialog, text='Số lượng:').grid(row=1, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(dialog)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Button(dialog, text='Thêm', command=lambda: self.add_to_tree(dialog)).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        if not self.book_dict:
            messagebox.showwarning("Cảnh báo", "Không có sách trong hệ thống. Vui lòng thêm sách trước.")
            return
    
    def add_to_tree(self, dialog):
        book_name = self.book_var.get()
        try:
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số lượng hợp lệ")
            return
        
        if not book_name:
            messagebox.showerror("Lỗi", "Vui lòng chọn sách")
            return
        
        if book_name not in self.book_dict:
            messagebox.showerror("Lỗi", "Không tìm thấy sách")
            return
        
        # Lấy thông tin sách từ book_dict
        book_id, genre, import_price = self.book_dict[book_name]
        selling_price = import_price * 1.05  # Giá bán = 105% giá nhập, theo processing.py
        
        # Tạo số thứ tự (STT) dựa trên số hàng hiện có trong Treeview
        stt = len(self.tree.get_children()) + 1
        
        # Chèn dữ liệu vào Treeview
        self.tree.insert('', 'end', values=(stt, book_id, book_name, genre, quantity, selling_price))
        
        # Đóng dialog
        dialog.destroy()

    def save_invoice(self):
        customer_name = self.customer_var.get()
        if not customer_name:
            messagebox.showerror("Lỗi", "Vui lòng chọn hoặc thêm khách hàng")
            return
        if customer_name not in self.customer_dict:
            messagebox.showerror("Lỗi", f"Khách hàng '{customer_name}' không tồn tại")
            return
        customer_id = self.customer_dict[customer_name]
        
        date = self.date_entry.get()
        try:
            amount_paid = float(self.amount_paid_entry.get())
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số tiền trả hợp lệ")
            return
        
        items = []
        for child in self.tree.get_children():
            values = self.tree.item(child)['values']
            try:
                book_id = int(values[1])
                quantity = int(values[4])
                selling_price = float(values[5])
            except ValueError:
                messagebox.showerror("Lỗi", "Dữ liệu sách không hợp lệ")
                return
            items.append({
                'book_id': book_id,
                'name': values[2],
                'quantity': quantity,
                'selling_unit_price': selling_price
            })
        
        if not items:
            messagebox.showerror("Lỗi", "Không có sách nào trong hóa đơn")
            return
        
        invoice_data = {
            'customer_id': customer_id,
            'date': date,
            'amount_paid': amount_paid,
            'items': items
        }
        
        try:
            create_sales_invoice(self.db, invoice_data)
            messagebox.showinfo("Thành công", "Đã lưu hóa đơn")
            # Clear the form
            self.customer_var.set('')
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
            self.amount_paid_entry.delete(0, tk.END)
            for child in self.tree.get_children():
                self.tree.delete(child)
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    def remove_book(self):
        selected = self.tree.selection()
        if selected:
            self.tree.delete(selected)