from models import User
from storage import Storage

class UserManager:
    def __init__(self, filename):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        return Storage.load_from_json(self.filename)

    def save_users(self):
        Storage.save_to_json(self.users, self.filename)

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user.__dict__)
        self.save_users()

    def list_users(self):
        for user in self.users:
            print(f"Name: {user['name']}, User ID: {user['user_id']}")
