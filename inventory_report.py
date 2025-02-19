import sqlite3

def create_connection():
    return sqlite3.connect('bookstore.db')

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory_report (
            report_id INTEGER PRIMARY KEY AUTOINCREMENT,
            report_month TEXT NOT NULL,
            book_id INTEGER,
            title TEXT NOT NULL,
            initial_stock INTEGER NOT NULL,
            arise INTEGER NOT NULL,
            final_stock INTEGER NOT NULL,
            FOREIGN KEY(book_id) REFERENCES importing_books(id)
        )
    ''')
    conn.commit()
    conn.close()

def add_inventory_report(report_month, book_id, title, initial_stock, arise, final_stock):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO inventory_report (report_month, book_id, title, initial_stock, arise, final_stock)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (report_month, book_id, title, initial_stock, arise, final_stock))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    # Example usage
    # add_inventory_report("2025-02", 1, "Example Book", 10, 5, 15)
