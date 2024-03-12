class CheckInOut:
    def __init__(self, book_manager):
        self.book_manager = book_manager

    def check_out(self, books):
        if not books:
            print("Error: No books to check out.")
            return False

        for book in books:
            if not book.checked_out:
                book.checked_out = True
                print(f"Book '{book.title}' with ISBN '{book.isbn}' checked out successfully.")
            else:
                print(f"Error: Book '{book.title}' with ISBN '{book.isbn}' is already checked out.")
        self.book_manager.save_books()  # Save the updated book data
        return True

        
    def check_in(self, books):
        if not books:
            print("Error: Book not found.")
            return False

        for book in books:
            if not book.checked_out:
                print(f"Error: Book '{book.title}' with ISBN '{book.isbn}' is not checked out.")
            else:
                book.checked_out = False
                print(f"Book '{book.title}' with ISBN '{book.isbn}' checked in successfully.")
        return True