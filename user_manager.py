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
        user_list = []
        for user in self.users:
            user_info = f"Name: {user['name']}, User ID: {user['user_id']}"
            print(user_info)
            user_list.append(user_info)
        return user_list

    def find_user_by_name(self, name):
        if isinstance(name, str):
            return [user for user in self.users if name.lower() in user['name'].lower()]

    def find_user_by_id(self, user_id):
        return [user for user in self.users if str(user_id).lower() == str(user['user_id']).lower()]


    def delete_user(self, user_id):
        initial_length = len(self.users)
        self.users = [user for user in self.users if user['user_id'] != user_id]
        if len(self.users) < initial_length:
            self.save_users()
            print("User deleted successfully.")
            return True  # Indicate successful deletion
        else:
            print("User not found.")
            return False


    def update_user(self, old_user_id, new_name, new_user_id):
        for user in self.users:
            if str(user['user_id']).lower() == str(old_user_id).lower():
                user['name'] = new_name
                user['user_id'] = new_user_id  # Update the user ID
                self.save_users()
                print("User updated successfully.")
                return True

        print("User not found.")
        return False