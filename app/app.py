import tkinter as tk
from tkinter import ttk
import os
from database import Database
from gui_import_receipt import ImportReceiptForm
from gui_sales_invoice import SalesInvoiceForm
from gui_book_list import BookListForm
from gui_payment_receipt import PaymentReceiptForm
from gui_inventory_report import InventoryReportForm
from gui_debt_report import DebtReportForm
from gui_settings import SettingsForm

class BookstoreApp:
    def __init__(self, root):
        print("Thư mục hiện tại:", os.getcwd())
        os.makedirs('data', exist_ok=True)  # Tạo thư mục 'data' nếu chưa tồn tại
        self.root = root
        self.root.title("Quản lý nhà sách")
        self.db = Database('data/bookstore.db')  # Sử dụng đường dẫn tuyệt đối
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)
        
        self.import_receipt_tab = tk.Frame(self.notebook)
        self.notebook.add(self.import_receipt_tab, text='Phiếu nhập sách')
        ImportReceiptForm(self.import_receipt_tab, self.db)
        
        self.sales_invoice_tab = tk.Frame(self.notebook)
        self.notebook.add(self.sales_invoice_tab, text='Hóa đơn bán sách')
        SalesInvoiceForm(self.sales_invoice_tab, self.db)
        
        self.book_list_tab = tk.Frame(self.notebook)
        self.notebook.add(self.book_list_tab, text='Danh sách sách')
        BookListForm(self.book_list_tab, self.db)
        
        self.payment_receipt_tab = tk.Frame(self.notebook)
        self.notebook.add(self.payment_receipt_tab, text='Phiếu thu tiền')
        PaymentReceiptForm(self.payment_receipt_tab, self.db)
        
        self.inventory_report_tab = tk.Frame(self.notebook)
        self.notebook.add(self.inventory_report_tab, text='Báo cáo tồn kho')
        InventoryReportForm(self.inventory_report_tab, self.db)
        
        self.debt_report_tab = tk.Frame(self.notebook)
        self.notebook.add(self.debt_report_tab, text='Báo cáo công nợ')
        DebtReportForm(self.debt_report_tab, self.db)
        
        self.settings_tab = tk.Frame(self.notebook)
        self.notebook.add(self.settings_tab, text='Cài đặt')
        SettingsForm(self.settings_tab, self.db)
    
    def __del__(self):
        self.db.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreApp(root)
    root.mainloop()