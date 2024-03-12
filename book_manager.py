from storage import Storage
from book import Book

class BookManager:
    def __init__(self, filename):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        data = Storage.load_from_json(self.filename)
        books = []
        for book_data in data:
            book = Book(book_data['title'], book_data['author'], book_data['isbn'])
            book.checked_out = book_data['checked_out']
            books.append(book)
        return books

    def save_books(self):
        Storage.save_to_json([book.to_dict() for book in self.books], self.filename)

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_books()

    def list_books(self):
        book_list = []
        for index, book in enumerate(self.books, start=1):
            book_info = f"{index}. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Checked Out: {book.checked_out}"
            print(book_info)
            book_list.append(book_info)
        return book_list

    def find_book_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def find_book_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def find_book_by_isbn(self, isbn):
        return [book for book in self.books if isbn.lower() == book.isbn.lower()]

    def delete_books_by_isbn(self, isbn):
        isbn = str(isbn)
        initial_length = len(self.books)
        print(f"Initial number of books: {initial_length}")
        print(f"Books ISBNs: {[book.isbn for book in self.books]}")

        # Ensure the provided ISBN is a string
        if not isinstance(isbn, str):
            print("Error: Provided ISBN must be a string.")
            return False

        # Convert both the stored ISBNs and the provided ISBN to lowercase for case-insensitive comparison
        lower_isbn = isbn.lower()

        print(f"Provided ISBN (lowercase): {lower_isbn}")

        self.books = [book for book in self.books if str(book.isbn).lower() != lower_isbn]

        print(f"Books ISBNs after deletion: {[book.isbn for book in self.books]}")

        if len(self.books) < initial_length:
            self.save_books()
            print("Books with the given ISBN deleted successfully.")
            return True  # Indicate successful deletion
        else:
            print("No books found with the given ISBN.")
            return False

    def update_book(self, old_isbn, new_title, new_author, new_isbn):
        for book in self.books:
            if str(book.isbn).lower() == str(old_isbn).lower():
                book.title = new_title
                book.author = new_author
                book.isbn = new_isbn  # Update the ISBN
                self.save_books()
                print("Book updated successfully.")
                return True

        print("Book not found.")
        return False
