import getpass

class UserManager:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def register_user(self, username, password):
        if username in self.users:
            return False, "Username already exists."
        self.users[username] = password
        return True, "Registration successful!"

    def login_user(self, username, password):
        if self.users.get(username) == password:
            self.current_user = username
            return True, "Login successful!"
        else:
            return False, "Invalid username or password."

    def is_logged_in(self):
        return self.current_user is not None
