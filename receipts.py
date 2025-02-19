import sqlite3

def create_connection():
    return sqlite3.connect('bookstore.db')

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS receipts (
            receipt_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            address TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            receipt_date DATE NOT NULL,
            amount REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_receipt(customer_name, address, email, phone_number, receipt_date, amount):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO receipts (customer_name, address, email, phone_number, receipt_date, amount)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (customer_name, address, email, phone_number, receipt_date, amount))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    # Example usage
    # add_receipt("Jane Doe", "123 Main St", "jane@example.com", "1234567890", "2025-02-18", 100.50)
