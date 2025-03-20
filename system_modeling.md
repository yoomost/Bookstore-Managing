Use case diagram
----
Actors: Bookstore Manager, Cashier, Inventory Manager

Use cases:
- Import books
- View book list
- Create book invoices
- Manage receipts
- Inventory Report
- Debt Report

Class Diagram
---
Book
- Attributes: id, title, genre, stock, cost_price, sell_price
- Methods: add_book(), update_stock(), view_details()

Invoice
- Attributes: invoice_id, customer_name, invoice_date, book_id, quantity, total_price
- Methods: create_invoice(), calculate_total_price()

Receipt
- Attributes: receipt_id, customer_name, address, email, phone_number, receipt_date, amount
- Methods: create_receipt(), view_receipt()

Report
- Attributes: report_id, report_month, book_id, initial_stock, arise, final_stock
- Methods: generate_inventory_report(), generate_debt_report()

Entity-Relationship Diagram (ERD)
---
Books Table
- Fields: id, title, genre, stock, cost_price
- Relationships: One-to-many relationship with invoices and reports.

Invoices Table
- Fields: invoice_id, customer_name, invoice_date, book_id, quantity, sell_price

Receipts Table
- Fields: receipt_id, customer_name, address, email, phone_number, receipt_date, amount

Reports Table
- Fields: report_id, report_month, book_id, initial_stock, arise, final_stock
- Relationships: Linked to books via book_id.

Sequence Diagram
---
Based on Use cases

E.g. Create book invoices
- User action: Actor inputs customer name, book title and quantity
- System action:
-     The system retrieves book details (id, genre, cost_price) from the database.
-     Calculates sell_price = cost_price × 1.05.
-     Creates a new invoice with the provided details and stores it in the database.
- System Response: Confirmation of invoice creation is displayed to the user.

Activity Diagram
---
Based on Use cases

E.g. Import books

Start: User chooses to import books.

Input: User enters book details (title, genre, stock, cost_price).

Validation: The system checks for missing or invalid data.

Database Update: The system inserts the new book into the Books table.

End: The system displays a success message.

