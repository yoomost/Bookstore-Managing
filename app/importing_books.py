import sqlite3

def create_connection():
    return sqlite3.connect('bookstore.db')

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS importing_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            stock INTEGER NOT NULL,
            cost_price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_book(title, genre, stock, cost_price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO importing_books (title, genre, stock, cost_price)
        VALUES (?, ?, ?, ?)
    ''', (title, genre, stock, cost_price))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    # Example usage
    # add_book("Example Book", "Fiction", 10, 15.99)
