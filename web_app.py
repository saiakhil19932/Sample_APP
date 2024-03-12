import streamlit as st
from user_manager import UserManager
from book_manager import BookManager
from check import CheckInOut
import pandas as pd

def main():
    user_manager = UserManager('users.json')
    book_manager = BookManager('books.json')
    check_manager = CheckInOut(book_manager)

    st.title("Library Management System")

    menu = st.sidebar.selectbox("Menu", ["Add User", "List Users", "Add Book", "List Books", 
                                         "Search Book", "Check Out Book", "Check In Book", 
                                         "Delete Book", "Update Book", "Search User", 
                                         "Delete User", "Update User"])

    if menu == "Add User":
        st.subheader("Add User")
        name = st.text_input("Enter user's name:")
        user_id = st.text_input("Enter user's ID:")
        if st.button("Add User"):
            user_manager.add_user(name, user_id)
            st.success("User added successfully.")

    elif menu == "List Users":
        st.subheader("List Users")
        users = user_manager.list_users()
        print(users,"---------------")
        if users is not None:
            # for user in users:
            st.write(users)
        else:
            st.write("No users found.")

    elif menu == "Add Book":
        st.subheader("Add Book")
        title = st.text_input("Enter book's title:")
        author = st.text_input("Enter book's author:")
        isbn = st.text_input("Enter book's ISBN:")
        if st.button("Add Book"):
            book_manager.add_book(title, author, isbn)
            st.success("Book added successfully.")

    elif menu == "List Books":
        st.subheader("List Books")
        books = book_manager.list_books()
        if books is not None:
            # for book in books:
            st.write(books)
        else:
            st.write("No books found.")

    elif menu == "Search Book":
        st.subheader("Search Book")
        search_by = st.radio("Search by", ["Title", "Author", "ISBN"])
        search_term = st.text_input("Enter search term:")
        if st.button("Search"):
            if search_by == "Title":
                books = book_manager.find_book_by_title(search_term)
            elif search_by == "Author":
                books = book_manager.find_book_by_author(search_term)
            elif search_by == "ISBN":
                books = book_manager.find_book_by_isbn(search_term)

            if books:
                for book in books:
                    st.write(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Checked Out: {book.checked_out}")
            else:
                st.write("No books found.")

    elif menu == "Check Out Book":
        st.subheader("Check Out Book")
        isbn = st.text_input("Enter book's ISBN:")
        if st.button("Check Out"):
            book = book_manager.find_book_by_isbn(isbn)
            if book:
                if check_manager.check_out(book):
                    st.success("Book checked out successfully.")
                    book_manager.save_books()
                else:
                    st.warning("Book is already checked out.")
            else:
                st.error("Book not found.")

    elif menu == "Check In Book":
        st.subheader("Check In Book")
        isbn = st.text_input("Enter book's ISBN:")
        if st.button("Check In"):
            book = book_manager.find_book_by_isbn(isbn)
            if book:
                if check_manager.check_in(book):
                    st.success("Book checked in successfully.")
                    book_manager.save_books()
                else:
                    st.warning("Book is not checked out.")
            else:
                st.error("Book not found.")

    elif menu == "Delete Book":
        st.subheader("Delete Book")
        isbn = st.text_input("Enter book's ISBN:")
        if st.button("Delete Book"):
            book = book_manager.find_book_by_isbn(isbn)
            if book:
                book_manager.delete_books_by_isbn(isbn)
                st.success("Book deleted successfully.")
            else:
                st.error("Book not found.")

    elif menu == "Update Book":
        st.subheader("Update Book")
        old_isbn = st.text_input("Enter book's old ISBN:")
        new_title = st.text_input("Enter new title:")
        new_author = st.text_input("Enter new author:")
        new_isbn = st.text_input("Enter new ISBN:")
        if st.button("Update Book"):
            if book_manager.update_book(old_isbn, new_title, new_author, new_isbn):
                st.success("Book updated successfully.")
            else:
                st.error("Book not found.")

    elif menu == "Search User":
        st.subheader("Search User")
        search_by = st.radio("Search by", ["Name", "User ID"])
        search_term = st.text_input("Enter search term:")
        if st.button("Search"):
            if search_by == "Name":
                users = user_manager.find_user_by_name(search_term)
            elif search_by == "User ID":
                users = user_manager.find_user_by_id(search_term)

            if users:
                for user in users:
                    st.write(f"Name: {user['name']}, User ID: {user['user_id']}")
            else:
                st.write("No users found.")

    elif menu == "Delete User":
        st.subheader("Delete User")
        user_id = st.text_input("Enter user's ID:")
        if st.button("Delete User"):
            user_manager.delete_user(user_id)
            st.success("User deleted successfully.")

    elif menu == "Update User":
        st.subheader("Update User")
        user_id = st.text_input("Enter user's ID:")
        new_name = st.text_input("Enter new name:")
        new_user_id = st.text_input("Enter new user ID:")
        if st.button("Update User"):
            if user_manager.update_user(user_id, new_name, new_user_id):
                st.success("User updated successfully.")
            else:
                st.error("User not found.")

if __name__ == "__main__":
    main()
