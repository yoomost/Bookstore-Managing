import tkinter as tk
from tkinter import messagebox

class SettingsForm:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        
        # Minimum import quantity
        tk.Label(parent, text='Số lượng nhập tối thiểu:').grid(row=0, column=0, padx=5, pady=5)
        self.min_import_qty_entry = tk.Entry(parent)
        self.min_import_qty_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Maximum stock for import
        tk.Label(parent, text='Lượng tồn tối đa để nhập:').grid(row=1, column=0, padx=5, pady=5)
        self.max_stock_import_entry = tk.Entry(parent)
        self.max_stock_import_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Maximum debt for sale
        tk.Label(parent, text='Nợ tối đa để bán:').grid(row=2, column=0, padx=5, pady=5)
        self.max_debt_sale_entry = tk.Entry(parent)
        self.max_debt_sale_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Minimum stock after sale
        tk.Label(parent, text='Lượng tồn tối thiểu sau bán:').grid(row=3, column=0, padx=5, pady=5)
        self.min_stock_after_sale_entry = tk.Entry(parent)
        self.min_stock_after_sale_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Restrict payment
        tk.Label(parent, text='Hạn chế thu tiền không vượt nợ:').grid(row=4, column=0, padx=5, pady=5)
        self.restrict_payment_var = tk.BooleanVar()
        tk.Checkbutton(parent, variable=self.restrict_payment_var).grid(row=4, column=1, padx=5, pady=5)
        
        # Save button
        tk.Button(parent, text='Lưu cài đặt', command=self.save_settings).grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
        # Load current settings
        self.load_settings()
    
    def load_settings(self):
        settings = {
            'min_import_quantity': '150',
            'max_stock_for_import': '300',
            'max_debt_for_sale': '20000',
            'min_stock_after_sale': '20',
            'restrict_payment': 'True'
        }
        for key in settings:
            value = self.db.fetchone("SELECT value FROM Settings WHERE key = ?", (key,))
            if value:
                settings[key] = value[0]
        
        self.min_import_qty_entry.insert(0, settings['min_import_quantity'])
        self.max_stock_import_entry.insert(0, settings['max_stock_for_import'])
        self.max_debt_sale_entry.insert(0, settings['max_debt_for_sale'])
        self.min_stock_after_sale_entry.insert(0, settings['min_stock_after_sale'])
        self.restrict_payment_var.set(settings['restrict_payment'] == 'True')
    
    def save_settings(self):
        settings = {
            'min_import_quantity': self.min_import_qty_entry.get(),
            'max_stock_for_import': self.max_stock_import_entry.get(),
            'max_debt_for_sale': self.max_debt_sale_entry.get(),
            'min_stock_after_sale': self.min_stock_after_sale_entry.get(),
            'restrict_payment': str(self.restrict_payment_var.get())
        }
        for key, value in settings.items():
            self.db.execute("INSERT OR REPLACE INTO Settings (key, value) VALUES (?, ?)", (key, value))
        self.db.conn.commit()
        messagebox.showinfo("Thành công", "Đã lưu cài đặt")