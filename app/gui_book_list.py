import tkinter as tk
from tkinter import ttk

class BookListForm:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        
        # Tạo Treeview để hiển thị danh sách sách
        self.tree = ttk.Treeview(parent, columns=('STT', 'Name', 'Genre', 'Author', 'Stock'), show='headings')
        self.tree.heading('STT', text='STT')
        self.tree.heading('Name', text='Tên sách')
        self.tree.heading('Genre', text='Thể loại')
        self.tree.heading('Author', text='Tác giả')
        self.tree.heading('Stock', text='Số lượng')
        self.tree.pack(fill='both', expand=True)
        
        # Thêm nút Refresh
        tk.Button(parent, text="Refresh", command=self.load_books).pack(pady=10)
        
        # Tải dữ liệu ban đầu
        self.load_books()
    
    def load_books(self):
        # Xóa dữ liệu cũ trong Treeview
        for child in self.tree.get_children():
            self.tree.delete(child)
        # Truy vấn database để lấy danh sách sách mới nhất
        books = self.db.fetchall("SELECT book_id, name, genre, author, stock FROM Books")
        # Thêm dữ liệu mới vào Treeview
        for i, book in enumerate(books, start=1):
            self.tree.insert('', 'end', values=(i, book[1], book[2], book[3], book[4]))