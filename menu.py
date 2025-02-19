import importing_books
import book_invoices
import book_list
import receipts
import inventory_report
import debt_report

def main_menu():
    while True:
        print("\nQUẢN LÝ NHÀ SÁCH")
        print("1. Phiếu nhập sách")
        print("2. Hoá đơn bán sách")
        print("3. Danh sách Sách")
        print("4. Phiếu thu tiền")
        print("5. Báo cáo tồn")
        print("6. Báo cáo công nợ")
        print("7. Thoát")

        choice = input("Chọn chức năng (1-7): ")

        if choice == "1":
            importing_books_menu()
        elif choice == "2":
            book_invoices_menu()
        elif choice == "3":
            book_list_menu()
        elif choice == "4":
            receipts_menu()
        elif choice == "5":
            inventory_report_menu()
        elif choice == "6":
            debt_report_menu()
        elif choice == "7":
            break
        else:
            print("Invalid option. Please try again.")

def importing_books_menu():
    print("\nImport Books")
    title = input("Enter book title: ")
    genre = input("Enter book genre: ")
    stock = int(input("Enter stock quantity: "))
    cost_price = float(input("Enter cost price: "))
    importing_books.add_book(title, genre, stock, cost_price)
    print("Book imported successfully!")

def book_invoices_menu():
    print("\nBook Invoices")
    customer_name = input("Enter customer name: ")
    title = input("Enter book title: ")
    quantity = int(input("Enter quantity: "))
    book_invoices.add_invoice(customer_name, title, quantity)

def book_list_menu():
    print("\nBook List")
    book_list.show_books()

def receipts_menu():
    print("\nReceipts")
    customer_name = input("Enter customer name: ")
    address = input("Enter address: ")
    email = input("Enter email: ")
    phone_number = input("Enter phone number: ")
    receipt_date = input("Enter receipt date (YYYY-MM-DD): ")
    amount = float(input("Enter amount: "))
    receipts.add_receipt(customer_name, address, email, phone_number, receipt_date, amount)
    print("Receipt added successfully!")

def inventory_report_menu():
    print("\nInventory Report")
    report_month = input("Enter report month (YYYY-MM): ")
    book_id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    initial_stock = int(input("Enter initial stock: "))
    arise = int(input("Enter arise quantity: "))
    final_stock = int(input("Enter final stock: "))
    inventory_report.add_inventory_report(report_month, book_id, title, initial_stock, arise, final_stock)
    print("Inventory report added successfully!")

def debt_report_menu():
    print("\nDebt Report")
    report_month = input("Enter report month (YYYY-MM): ")
    customer_id = int(input("Enter customer ID: "))
    customer_name = input("Enter customer name: ")
    initial_debt = float(input("Enter initial debt: "))
    arise = float(input("Enter arise amount: "))
    final_debt = float(input("Enter final debt: "))
    debt_report.add_debt_report(report_month, customer_id, customer_name, initial_debt, arise, final_debt)
    print("Debt report added successfully!")

if __name__ == "__main__":
    main_menu()
