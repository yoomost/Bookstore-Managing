import tkinter as tk
from tkinter import ttk, messagebox
import importing_books
import book_invoices
import book_list
import receipts
import inventory_report
import debt_report

class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookstore Management Menu")
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill='both', expand=True)

        # Display the main menu
        self.main_menu()

    def main_menu(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Bookstore Management Menu", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(self.main_frame, text="Import Books", command=self.import_books_menu).pack(fill='x', pady=5)
        tk.Button(self.main_frame, text="Book Invoices", command=self.book_invoices_menu).pack(fill='x', pady=5)
        tk.Button(self.main_frame, text="Show Book List", command=self.book_list_menu).pack(fill='x', pady=5)
        tk.Button(self.main_frame, text="Receipts", command=self.receipts_menu).pack(fill='x', pady=5)
        tk.Button(self.main_frame, text="Inventory Report", command=self.inventory_report_menu).pack(fill='x', pady=5)
        tk.Button(self.main_frame, text="Debt Report", command=self.debt_report_menu).pack(fill='x', pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit).pack(fill='x', pady=5)

    def import_books_menu(self):
        self.clear_frame()
        self.build_form("Import Books", self.add_book, import_books=True)

    def book_invoices_menu(self):
        self.clear_frame()
        self.build_form("Book Invoices", self.add_invoice, book_invoices=True)

    def book_list_menu(self):
        self.clear_frame()
        books = book_list.show_books()
        
        if books:
            tree = ttk.Treeview(self.main_frame, columns=("ID", "Title", "Genre", "Stock", "Cost Price"), show="headings")
            tree.heading("ID", text="ID")
            tree.heading("Title", text="Title")
            tree.heading("Genre", text="Genre")
            tree.heading("Stock", text="Stock")
            tree.heading("Cost Price", text="Cost Price")
            
            for book in books:
                tree.insert("", tk.END, values=book)
            
            tree.pack(fill='both', expand=True)
        else:
            tk.Label(self.main_frame, text="No books found.").pack()

        tk.Button(self.main_frame, text="Back", command=self.main_menu).pack(pady=5)

    def receipts_menu(self):
        self.clear_frame()
        self.build_form("Receipts", self.add_receipt, receipt_form=True)

    def inventory_report_menu(self):
        self.clear_frame()
        self.build_form("Inventory Report", self.add_inventory_report, report_form=True)

    def debt_report_menu(self):
        self.clear_frame()
        self.build_form("Debt Report", self.add_debt_report, debt_form=True)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def build_form(self, title, command, import_books=False, book_invoices=False, receipt_form=False, report_form=False, debt_form=False):
        tk.Label(self.main_frame, text=title, font=("Helvetica", 16)).pack(pady=10)

        self.entries = {}

        if import_books:
            self.add_entry("title", "Title")
            self.add_entry("genre", "Genre")
            self.add_entry("stock", "Stock")
            self.add_entry("cost_price", "Cost Price")
        elif book_invoices:
            self.add_entry("customer_name", "Customer Name")
            self.add_entry("title", "Title")
            self.add_entry("quantity", "Quantity")

        if receipt_form:
            self.add_entry("customer_name", "Customer Name")
            self.add_entry("address", "Address")
            self.add_entry("email", "Email")
            self.add_entry("phone_number", "Phone Number")
            self.add_entry("receipt_date", "Receipt Date (YYYY-MM-DD)")
            self.add_entry("amount", "Amount")

        if report_form:
            self.add_entry("report_month", "Report Month (YYYY-MM)")
            self.add_entry("book_id", "Book ID")
            self.add_entry("initial_stock", "Initial Stock")
            self.add_entry("arise", "Arise Quantity")
            self.add_entry("final_stock", "Final Stock")

        if debt_form:
            self.add_entry("report_month", "Report Month (YYYY-MM)")
            self.add_entry("customer_id", "Customer ID")
            self.add_entry("initial_debt", "Initial Debt")
            self.add_entry("arise", "Arise Amount")
            self.add_entry("final_debt", "Final Debt")

        tk.Button(self.main_frame, text="Submit", command=command).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.main_menu).pack(pady=5)

    def add_entry(self, key, label_text):
        tk.Label(self.main_frame, text=label_text).pack()
        entry = tk.Entry(self.main_frame)
        entry.pack()
        self.entries[key] = entry

    def add_book(self):
        title = self.entries["title"].get()
        genre = self.entries["genre"].get()
        stock = int(self.entries["stock"].get())
        cost_price = float(self.entries["cost_price"].get())
        importing_books.add_book(title, genre, stock, cost_price)
        messagebox.showinfo("Success", "Book imported successfully!")
        self.main_menu()

    def add_invoice(self):
        customer_name = self.entries["customer_name"].get()
        title = self.entries["title"].get()
        quantity = int(self.entries["quantity"].get())
        book_invoices.add_invoice(customer_name, title, quantity)
        messagebox.showinfo("Success", "Invoice added successfully!")
        self.main_menu()

    def add_receipt(self):
        customer_name = self.entries["customer_name"].get()
        address = self.entries["address"].get()
        email = self.entries["email"].get()
        phone_number = self.entries["phone_number"].get()
        receipt_date = self.entries["receipt_date"].get()
        amount = float(self.entries["amount"].get())
        receipts.add_receipt(customer_name, address, email, phone_number, receipt_date, amount)
        messagebox.showinfo("Success", "Receipt added successfully!")
        self.main_menu()

    def add_inventory_report(self):
        report_month = self.entries["report_month"].get()
        book_id = int(self.entries["book_id"].get())
        title = self.entries["title"].get()
        initial_stock = int(self.entries["initial_stock"].get())
        arise = int(self.entries["arise"].get())
        final_stock = int(self.entries["final_stock"].get())
        inventory_report.add_inventory_report(report_month, book_id, title, initial_stock, arise, final_stock)
        messagebox.showinfo("Success", "Inventory report added successfully!")
        self.main_menu()

    def add_debt_report(self):
        report_month = self.entries["report_month"].get()
        customer_id = int(self.entries["customer_id"].get())
        customer_name = self.entries["customer_name"].get()
        initial_debt = float(self.entries["initial_debt"].get())
        arise = float(self.entries["arise"].get())
        final_debt = float(self.entries["final_debt"].get())
        debt_report.add_debt_report(report_month, customer_id, customer_name, initial_debt, arise, final_debt)
        messagebox.showinfo("Success", "Debt report added successfully!")
        self.main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreApp(root)
    root.mainloop()
