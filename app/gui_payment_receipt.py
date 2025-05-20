import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from processing import create_payment_receipt

class PaymentReceiptForm:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        
        # Customer selection
        tk.Label(parent, text='Khách hàng:').grid(row=0, column=0, padx=5, pady=5)
        customers = self.db.fetchall("SELECT customer_id, name FROM Customers")
        self.customer_dict = {c[1]: c[0] for c in customers}
        self.customer_var = tk.StringVar()
        ttk.Combobox(parent, textvariable=self.customer_var, values=list(self.customer_dict.keys())).grid(row=0, column=1, padx=5, pady=5)
        
        # Date entry
        tk.Label(parent, text='Ngày thu:').grid(row=1, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(parent)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)
        self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
        
        # Amount collected entry
        tk.Label(parent, text='Số tiền thu:').grid(row=2, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(parent)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Save button
        tk.Button(parent, text='Lưu phiếu', command=self.save_receipt).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    
    def save_receipt(self):
        customer_name = self.customer_var.get()
        if not customer_name:
            messagebox.showerror("Lỗi", "Vui lòng chọn khách hàng")
            return
        customer_id = self.customer_dict[customer_name]
        date = self.date_entry.get()
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số tiền hợp lệ")
            return
        receipt_data = {
            'customer_id': customer_id,
            'date': date,
            'amount_collected': amount
        }
        try:
            create_payment_receipt(self.db, receipt_data)
            messagebox.showinfo("Thành công", "Đã lưu phiếu thu")
            self.customer_var.set('')
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
            self.amount_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))