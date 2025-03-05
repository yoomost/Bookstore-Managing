import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect('bookstore.db')
        print("Connection successful!")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def show_books():
    conn = create_connection()
    books = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT id, title, genre, stock, cost_price FROM importing_books')
            books = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")
    return books

if __name__ == "__main__":
    books = show_books()
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Genre: {book[2]}, Stock: {book[3]}, Cost Price: {book[4]}")
