import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from processing import create_import_receipt

class ImportReceiptForm:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        
        # Date entry
        tk.Label(parent, text='Ngày nhập:').grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(parent)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
        self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
        
        # Treeview for books
        self.tree = ttk.Treeview(parent, columns=('STT', 'Book ID', 'Name', 'Genre', 'Author', 'Quantity', 'Import Price'), show='headings')
        self.tree.heading('STT', text='STT')
        self.tree.heading('Book ID', text='Mã sách')
        self.tree.heading('Name', text='Tên sách')
        self.tree.heading('Genre', text='Thể loại')
        self.tree.heading('Author', text='Tác giả')
        self.tree.heading('Quantity', text='Số lượng')
        self.tree.heading('Import Price', text='Đơn giá nhập')
        self.tree.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        # Buttons
        tk.Button(parent, text='Thêm sách', command=self.add_book).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(parent, text='Xóa sách', command=self.remove_book).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(parent, text='Lưu phiếu', command=self.save_receipt).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    
    def add_book(self):
        dialog = tk.Toplevel(self.parent)
        
        # Toggle function for new/existing book
        def toggle_new_book():
            if self.new_book_var.get():
                self.book_combobox.config(state='disabled')
                self.new_name_entry.config(state='normal')
                self.new_genre_entry.config(state='normal')
                self.new_author_entry.config(state='normal')
            else:
                self.book_combobox.config(state='readonly')
                self.new_name_entry.config(state='disabled')
                self.new_genre_entry.config(state='disabled')
                self.new_author_entry.config(state='disabled')
        
        # Checkbox for new book
        self.new_book_var = tk.BooleanVar(value=False)
        tk.Checkbutton(dialog, text="Sách mới", variable=self.new_book_var, command=toggle_new_book).grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        # Combobox for existing books
        tk.Label(dialog, text='Sách:').grid(row=1, column=0, padx=5, pady=5)
        books = self.db.fetchall("SELECT book_id, name, genre, author FROM Books")
        self.book_dict = {b[1]: (b[0], b[2], b[3]) for b in books}
        self.book_var = tk.StringVar()
        self.book_combobox = ttk.Combobox(dialog, textvariable=self.book_var, values=list(self.book_dict.keys()), state='readonly')
        self.book_combobox.grid(row=1, column=1, padx=5, pady=5)
        
        # Entry fields for new book
        tk.Label(dialog, text='Tên sách:').grid(row=2, column=0, padx=5, pady=5)
        self.new_name_entry = tk.Entry(dialog, state='disabled')
        self.new_name_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(dialog, text='Thể loại:').grid(row=3, column=0, padx=5, pady=5)
        self.new_genre_entry = tk.Entry(dialog, state='disabled')
        self.new_genre_entry.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(dialog, text='Tác giả:').grid(row=4, column=0, padx=5, pady=5)
        self.new_author_entry = tk.Entry(dialog, state='disabled')
        self.new_author_entry.grid(row=4, column=1, padx=5, pady=5)
        
        # Quantity and Price
        tk.Label(dialog, text='Số lượng:').grid(row=5, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(dialog)
        self.quantity_entry.grid(row=5, column=1, padx=5, pady=5)
        
        tk.Label(dialog, text='Đơn giá nhập:').grid(row=6, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(dialog)
        self.price_entry.grid(row=6, column=1, padx=5, pady=5)
        
        tk.Button(dialog, text='Thêm', command=lambda: self.add_to_tree(dialog)).grid(row=7, column=0, columnspan=2, padx=5, pady=5)
    
    def add_to_tree(self, dialog):
        if self.new_book_var.get():
            # New book
            name = self.new_name_entry.get()
            genre = self.new_genre_entry.get()
            author = self.new_author_entry.get()
            try:
                quantity = int(self.quantity_entry.get())
                price = float(self.price_entry.get())
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập số lượng và đơn giá hợp lệ")
                return
            if not name or not genre or not author:
                messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin sách mới")
                return
            stt = len(self.tree.get_children()) + 1
            self.tree.insert('', 'end', values=(stt, "NEW", name, genre, author, quantity, price))
        else:
            # Existing book
            book_name = self.book_var.get()
            if not book_name:
                messagebox.showerror("Lỗi", "Vui lòng chọn sách")
                return
            try:
                quantity = int(self.quantity_entry.get())
                price = float(self.price_entry.get())
            except ValueError:
                messagebox.showerror("Lỗi", "Vui lòng nhập số lượng và đơn giá hợp lệ")
                return
            if book_name not in self.book_dict:
                messagebox.showerror("Lỗi", "Không tìm thấy sách")
                return
            book_id, genre, author = self.book_dict[book_name]
            stt = len(self.tree.get_children()) + 1
            self.tree.insert('', 'end', values=(stt, book_id, book_name, genre, author, quantity, price))
        dialog.destroy()
    
    def remove_book(self):
        selected = self.tree.selection()
        if selected:
            self.tree.delete(selected)
    
    def save_receipt(self):
        date = self.date_entry.get()
        items = []
        for child in self.tree.get_children():
            values = self.tree.item(child)['values']
            if values[1] == "NEW":
                # Insert new book
                self.db.execute("INSERT INTO Books (name, genre, author, stock, import_unit_price) VALUES (?, ?, ?, 0, NULL)", (values[2], values[3], values[4]))
                new_book_id = self.db.cursor.lastrowid
                book_id = new_book_id
            else:
                book_id = int(values[1])
            items.append({
                'book_id': book_id,
                'quantity': int(values[5]),
                'import_unit_price': float(values[6])
            })
        try:
            create_import_receipt(self.db, {'date': date, 'items': items})
            messagebox.showinfo("Thành công", "Đã lưu phiếu nhập")
            for child in self.tree.get_children():
                self.tree.delete(child)
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))