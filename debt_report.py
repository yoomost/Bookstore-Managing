import sqlite3

def create_connection():
    return sqlite3.connect('bookstore.db')

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS debt_report (
            report_id INTEGER PRIMARY KEY AUTOINCREMENT,
            report_month TEXT NOT NULL,
            customer_id INTEGER,
            customer_name TEXT NOT NULL,
            initial_debt REAL NOT NULL,
            arise REAL NOT NULL,
            final_debt REAL NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES receipts(receipt_id)
        )
    ''')
    conn.commit()
    conn.close()

def add_debt_report(report_month, customer_id, customer_name, initial_debt, arise, final_debt):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO debt_report (report_month, customer_id, customer_name, initial_debt, arise, final_debt)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (report_month, customer_id, customer_name, initial_debt, arise, final_debt))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    # Example usage
    # add_debt_report("2025-02", 1, "Jane Doe", 100.0, 50.0, 150.0)
