import tkinter as tk
from tkinter import ttk, messagebox
import business_logic as bl  # Import the Business Logic Layer

class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookstore Management")
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill='both', expand=True)

        self.main_menu()

    def main_menu(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Bookstore Management Menu", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(self.main_frame, text="Import Books", command=self.import_books_menu).pack(fill='x', pady=5)
        tk.Button(self.main_frame, text="Book Invoices", command=self.create_invoice_menu).pack(fill='x', pady=5)
        tk.Button(self.main_frame, text="Show Book List", command=self.show_books).pack(fill='x', pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit).pack(fill='x', pady=5)

    def import_books_menu(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Import Books", font=("Helvetica", 16)).pack(pady=10)

        title = self.create_entry("Title:")
        genre = self.create_entry("Genre:")
        stock = self.create_entry("Stock:")
        cost_price = self.create_entry("Cost Price:")

        def submit():
            bl.import_books(title.get(), genre.get(), int(stock.get()), float(cost_price.get()))
            messagebox.showinfo("Success", "Book Imported Successfully!")
            self.main_menu()

        tk.Button(self.main_frame, text="Submit", command=submit).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.main_menu).pack(pady=5)

    def create_invoice_menu(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Create Invoice", font=("Helvetica", 16)).pack(pady=10)

        customer_name = self.create_entry("Customer Name:")
        title = self.create_entry("Book Title:")
        quantity = self.create_entry("Quantity:")

        def submit():
            bl.create_invoice(customer_name.get(), title.get(), int(quantity.get()))
            messagebox.showinfo("Success", "Invoice Created Successfully!")
            self.main_menu()

        tk.Button(self.main_frame, text="Submit", command=submit).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.main_menu).pack(pady=5)

    def show_books(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Book List", font=("Helvetica", 16)).pack(pady=10)

        books = bl.get_books()
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

    def create_entry(self, label_text):
        tk.Label(self.main_frame, text=label_text).pack()
        entry = tk.Entry(self.main_frame)
        entry.pack()
        return entry

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreApp(root)
    root.mainloop()
