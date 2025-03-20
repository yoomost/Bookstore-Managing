import sqlite3

def connect():
    return sqlite3.connect('bookstore.db')

def add_book(title, genre, stock, cost_price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO importing_books (title, genre, stock, cost_price)
        VALUES (?, ?, ?, ?)
    ''', (title, genre, stock, cost_price))
    conn.commit()
    conn.close()

def get_book_by_title(title):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, genre, stock, cost_price FROM importing_books WHERE title = ?', (title,))
    book = cursor.fetchone()
    conn.close()
    return {"id": book[0], "title": book[1], "genre": book[2], "stock": book[3], "cost_price": book[4]} if book else None

def update_stock(book_id, new_stock):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE importing_books SET stock = ? WHERE id = ?', (new_stock, book_id))
    conn.commit()
    conn.close()

def add_invoice(customer_name, book_id, quantity, total_price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO book_invoices (customer_name, book_id, quantity, sell_price)
        VALUES (?, ?, ?, ?)
    ''', (customer_name, book_id, quantity, total_price))
    conn.commit()
    conn.close()

def get_all_books():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, genre, stock, cost_price FROM importing_books')
    books = cursor.fetchall()
    conn.close()
    return books
