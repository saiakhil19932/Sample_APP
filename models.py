class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Checked Out: {self.checked_out}"

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'checked_out': self.checked_out
        }
