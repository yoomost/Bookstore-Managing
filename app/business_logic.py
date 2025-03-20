import data_access as dal  # Import the Data Access Layer

def import_books(title, genre, stock, cost_price):
    # Validate input
    if not title or not genre or stock < 0 or cost_price < 0:
        raise ValueError("Invalid input data for importing books.")
    # Call DAL to save book
    dal.add_book(title, genre, stock, cost_price)

def create_invoice(customer_name, title, quantity):
    # Fetch book details
    book = dal.get_book_by_title(title)
    if not book:
        raise ValueError("Book not found.")
    if book["stock"] < quantity:
        raise ValueError("Insufficient stock.")
    
    # Calculate total price
    sell_price = book["cost_price"] * 1.05
    total_price = sell_price * quantity

    # Update stock and save invoice
    dal.update_stock(book["id"], book["stock"] - quantity)
    dal.add_invoice(customer_name, book["id"], quantity, total_price)

def get_books():
    return dal.get_all_books()
