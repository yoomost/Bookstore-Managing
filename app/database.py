import sqlite3

class Database:
    def __init__(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
            self.create_tables()
            print(f"Đã kết nối thành công đến database: {db_file}")
        except sqlite3.Error as e:
            print(f"Lỗi khi kết nối đến database: {e}")
            raise

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                genre TEXT,
                author TEXT,
                stock INTEGER,
                import_unit_price REAL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT,
                phone TEXT,
                email TEXT,
                debt REAL DEFAULT 0
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Import_Receipts (
                receipt_id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Import_Receipt_Details (
                detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                receipt_id INTEGER,
                book_id INTEGER,
                quantity INTEGER,
                import_unit_price REAL,
                FOREIGN KEY (receipt_id) REFERENCES Import_Receipts(receipt_id),
                FOREIGN KEY (book_id) REFERENCES Books(book_id)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Sales_Invoices (
                invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                customer_id INTEGER,
                total_amount REAL,
                amount_paid REAL,
                remaining_amount REAL,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Sales_Invoice_Details (
                detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                invoice_id INTEGER,
                book_id INTEGER,
                quantity INTEGER,
                selling_unit_price REAL,
                FOREIGN KEY (invoice_id) REFERENCES Sales_Invoices(invoice_id),
                FOREIGN KEY (book_id) REFERENCES Books(book_id)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Payment_Receipts (
                receipt_id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                customer_id INTEGER,
                amount_collected REAL,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)
        self.conn.commit()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()