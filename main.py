import sys
sys.path.append("./")

from user_manager import UserManager
from book_manager import BookManager
from check import CheckInOut

def main():
    user_manager = UserManager('users.json')
    book_manager = BookManager('books.json')
    check_manager = CheckInOut(book_manager)

    while True:
        print("1. Add User")
        print("2. List Users")
        print("3. Add Book")
        print("4. List Books")
        print("5. Search Book")
        print("6. Check Out Book")
        print("7. Check In Book")
        print("8. Delete Book")
        print("9. Update Book")
        print("10. Search User")
        print("11. Delete User")
        print("12. Update User")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user's name: ")
            user_id = input("Enter user's ID: ")
            user_manager.add_user(name, user_id)
        elif choice == '2':
            user_manager.list_users()
        elif choice == '3':
            title = input("Enter book's title: ")
            author = input("Enter book's author: ")
            isbn = input("Enter book's ISBN: ")
            book_manager.add_book(title, author, isbn)
        elif choice == '4':
            book_manager.list_books()
        elif choice == '5':
            search_by = input("Search by (title/author/ISBN): ").lower()
            search_term = input("Enter search term: ")
            if search_by == 'title':
                books = book_manager.find_book_by_title(search_term)
            elif search_by == 'author':
                books = book_manager.find_book_by_author(search_term)
            elif search_by == 'isbn':
                books = book_manager.find_book_by_isbn(search_term)
            else:
                print("Invalid search criteria.")
                continue
            if books:
                for idx, book in enumerate(books, start=1):
                    print(f"{idx}. {book}")
            else:
                print("No books found.")
        elif choice == '6':
            isbn = input("Enter book's ISBN: ")
            book = book_manager.find_book_by_isbn(isbn)
            if book:
                if check_manager.check_out(book):
                    print("Book checked out successfully.")
                    book_manager.save_books()
                else:
                    print("Book is already checked out.")
            else:
                print("Book not found.")
        elif choice == '7':
            isbn = input("Enter book's ISBN: ")
            book = book_manager.find_book_by_isbn(isbn)
            if book:
                if check_manager.check_in(book):
                    print("Book checked in successfully.")
                    book_manager.save_books()
                else:
                    print("Book is not checked out.")
            else:
                print("Book not found.")
        elif choice == '8':
            isbn = input("Enter book's ISBN: ")
            book = book_manager.find_book_by_isbn(isbn)
            if book:
                book_manager.delete_books_by_isbn(isbn)
                print("Book deleted successfully.")
            else:
                print("Book not found.")
        elif choice == '9':
            old_isbn = input("Enter book's old ISBN: ")
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            new_isbn = input("Enter new ISBN: ")
            if book_manager.update_book(old_isbn, new_title, new_author, new_isbn):
                print("Book updated successfully.")
            else:
                print("Book not found.")
        elif choice == '10':
            search_by = input("Search by (name/user ID): ").lower()
            search_term = input("Enter search term: ")
            if search_by == 'name':
                users = user_manager.find_user_by_name(search_term)
            elif search_by == 'user id':
                users = user_manager.find_user_by_id(search_term)
            else:
                print("Invalid search criteria.")
                continue
            if users:
                for idx, user in enumerate(users, start=1):
                    print(f"{idx}. Name: {user['name']}, User ID: {user['user_id']}")
            else:
                print("No users found.")
        elif choice == '11':
            user_id = input("Enter user's ID: ")
            user_manager.delete_user(user_id)
        elif choice == '12':
            user = input("Enter user's ID: ")
            name = input("Enter new name: ")
            new_user_id = input("Enter new user ID: ")
            if user_manager.update_user(user, name, new_user_id):
                print("User updated successfully.")
            else:
                print("User not found.")
        elif choice == '13':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
