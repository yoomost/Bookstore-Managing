import sqlite3
from datetime import datetime

def create_connection():
    try:
        conn = sqlite3.connect('bookstore.db')
        print("Connection successful!")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS book_invoices (
                    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    invoice_date DATE NOT NULL,
                    customer_name TEXT NOT NULL,
                    book_id INTEGER,
                    title TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    sell_price REAL NOT NULL,
                    FOREIGN KEY(book_id) REFERENCES importing_books(id)
                )
            ''')
            conn.commit()
            print("Table created successfully!")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

def get_book_details(title):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, genre, cost_price FROM importing_books WHERE title = ?
            ''', (title,))
            book_details = cursor.fetchone()
            if book_details:
                return book_details
            else:
                print("Book not found.")
                return None
        except sqlite3.Error as e:
            print(f"Error fetching book details: {e}")
            return None
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

def add_invoice(customer_name, title, quantity):
    book_details = get_book_details(title)
    if book_details:
        book_id, genre, cost_price = book_details
        sell_price = 1.05 * cost_price
        invoice_date = datetime.today().strftime('%Y-%m-%d')
        
        conn = create_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO book_invoices (invoice_date, customer_name, book_id, title, genre, quantity, sell_price)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (invoice_date, customer_name, book_id, title, genre, quantity, sell_price))
                conn.commit()
                print("Invoice added successfully!")
            except sqlite3.Error as e:
                print(f"Error inserting data: {e}")
            finally:
                conn.close()
        else:
            print("Error! Cannot create the database connection.")
    else:
        print("Invoice creation failed due to missing book details.")

if __name__ == "__main__":
    create_table()
    # Example usage
    # customer_name = input("Enter customer name: ")
    # title = input("Enter book title: ")
    # quantity = int(input("Enter quantity: "))
    # add_invoice(customer_name, title, quantity)
