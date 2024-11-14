from user import User
from finance import Finance

class Admin(User):
    def __init__(self, username, password, role, permissions):
        super().__init__(username, password, role, permissions)

    def manage_users(self, users):
        """ Allows admin to manage users: add, update, delete """
        action = input("Choose an action: [add/update/delete]: ")
        if action == 'add':
            username = input("Enter new username: ")
            if username in users:
                print("User already exists.")
            else:
                password = input("Enter new password: ")
                role = input("Enter role (admin/employee): ")
                permissions = input("Enter permissions (comma separated): ").split(',')
                users[username] = User(username, password, role, permissions)
                print(f"User {username} added successfully.")
        elif action == 'update':
            username = input("Enter username to update: ")
            if username in users:
                user = users[username]
                new_username = input(f"Enter new username (current: {user.username}): ")
                new_password = input("Enter new password: ")
                new_role = input(f"Enter new role (current: {user.role}): ")
                new_permissions = input(f"Enter new permissions (comma separated, current: {', '.join(user.permissions)}): ").split(',')
                users[username] = User(new_username, new_password, new_role, new_permissions)
                print(f"User {username} updated successfully.")
            else:
                print("User not found.")
        elif action == 'delete':
            username = input("Enter username to delete: ")
            if username in users:
                del users[username]
                print(f"User {username} deleted successfully.")
            else:
                print("User not found.")
        else:
            print("Invalid action.")

    def manage_finances(self, finance):
        """ Allows admin to manage finances """
        new_balance = float(input(f"Enter new balance (current: {finance.balance}): "))
        finance.balance = new_balance
        print(f"Finance balance updated to {new_balance}.")
