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
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT id, title, genre, stock FROM importing_books')
            books = cursor.fetchall()
            if books:
                print("\nBook List:")
                print("{:<5} {:<30} {:<20} {:<10}".format("ID", "Title", "Genre", "Stock"))
                print("-" * 75)
                for book in books:
                    print("{:<5} {:<30} {:<20} {:<10}".format(book[0], book[1], book[2], book[3]))
            else:
                print("No books found.")
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    show_books()
