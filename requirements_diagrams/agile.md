Epics
---
- Manage Book Inventory
- Generate Book Invoices
- Create and View Reports

User Stories (Derived from the Epics)
---
Epic 1: Manage Book Inventory

User Story: "As a bookstore manager, I want to import books into the inventory so that I can keep track of available stock."

Acceptance Criteria:
- The system allows input of book details (title, genre, stock, cost price).
- The book is added to the importing_books table in the database.
- A confirmation message is displayed after successfully saving.

Epic 2: Generate Book Invoices

User Story: "As a bookstore manager, I want to create invoices for sales so that I can track revenue and stock changes."

Acceptance Criteria:
- The system allows input of customer name, book title, and quantity.
- The system fetches the cost price and calculates the selling price (cost price × 1.05).
- The stock is updated to reflect the sale.
- The invoice is added to the book_invoices table in the database.

Epic 3: Create and View Reports

User Story: "As a bookstore manager, I want to view an inventory report so that I can analyze stock levels monthly."

Acceptance Criteria:
- The system generates a report showing initial stock, stock changes, and final stock for each book.
- The report can be exported as a document for record-keeping.
