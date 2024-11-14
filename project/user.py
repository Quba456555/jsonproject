import json

class User:
    def __init__(self, username, password, role, permissions=None):
        self.username = username
        self.password = password
        self.role = role
        self.permissions = permissions if permissions else []

    @classmethod
    def from_json(cls, data):
        return cls(
            data['username'],
            data['password'],
            data['role'],
            data.get('permissions', [])
        )

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'role': self.role,
            'permissions': self.permissions
        }

def load_users(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return {user['username']: User.from_json(user) for user in data}

def save_users(filename, users):
    with open(filename, 'w') as file:
        json.dump([user.to_dict() for user in users.values()], file, indent=4)
