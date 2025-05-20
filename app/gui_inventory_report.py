import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from processing import get_inventory_report

class InventoryReportForm:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        
        # Month and year selection
        tk.Label(parent, text='Tháng:').grid(row=0, column=0, padx=5, pady=5)
        self.month_var = tk.StringVar()
        ttk.Combobox(parent, textvariable=self.month_var, values=[str(i) for i in range(1, 13)]).grid(row=0, column=1, padx=5, pady=5)
        self.month_var.set(str(datetime.now().month))
        
        tk.Label(parent, text='Năm:').grid(row=0, column=2, padx=5, pady=5)
        self.year_var = tk.StringVar()
        ttk.Combobox(parent, textvariable=self.year_var, values=[str(i) for i in range(2000, 2030)]).grid(row=0, column=3, padx=5, pady=5)
        self.year_var.set(str(datetime.now().year))
        
        # Generate report button
        tk.Button(parent, text='Tạo báo cáo', command=self.generate_report).grid(row=0, column=4, padx=5, pady=5)
        
        # Treeview for report
        self.tree = ttk.Treeview(parent, columns=('STT', 'Book Name', 'Beginning Stock', 'Transactions', 'Ending Stock'), show='headings')
        self.tree.heading('STT', text='STT')
        self.tree.heading('Book Name', text='Tên sách')
        self.tree.heading('Beginning Stock', text='Tồn đầu')
        self.tree.heading('Transactions', text='Phát sinh')
        self.tree.heading('Ending Stock', text='Tồn cuối')
        self.tree.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
    
    def generate_report(self):
        try:
            month = int(self.month_var.get())
            year = int(self.year_var.get())
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng chọn tháng và năm hợp lệ")
            return
        report = get_inventory_report(self.db, year, month)
        for child in self.tree.get_children():
            self.tree.delete(child)
        for i, item in enumerate(report, start=1):
            self.tree.insert('', 'end', values=(i, item['book_name'], item['beginning_stock'], item['transactions'], item['ending_stock']))