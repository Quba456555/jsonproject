import json
from admin import Admin
from user import load_users, save_users
from product import load_products, save_products
from finance import load_finances, save_finances
from employee import buy_product, sell_product

def main():
    users_filename = 'users.json'
    products_filename = 'products.json'
    finances_filename = 'finances.json'

    
    users = load_users(users_filename)
    products = load_products(products_filename)
    finances = load_finances(finances_filename)

    
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = users.get(username)

    if user and user.password == password:
        print(f"Welcome, {user.username}!")
        if user.role == 'admin':
            print("You are an Admin.")
            admin = Admin(user.username, user.password, user.role, user.permissions)
            while True:
                action = input("Choose an action: [manage_users/manage_finances/exit]: ")
                if action == 'manage_users':
                    admin.manage_users(users)
                elif action == 'manage_finances':
                    admin.manage_finances(finances)
                elif action == 'exit':
                    break
                else:
                    print("Invalid action.")
        elif user.role == 'employee':
            print("You are an Employee.")
            while True:
                action = input("Choose an action: [buy/sell/exit]: ")
                if action == 'buy':
                    buy_product(username, products, finances)
                elif action == 'sell':
                    sell_product(username, products, finances)
                elif action == 'exit':
                    break
                else:
                    print("Invalid action.")
        
        
        save_users(users_filename, users)
        save_products(products_filename, products)
        save_finances(finances_filename, finances)
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()
