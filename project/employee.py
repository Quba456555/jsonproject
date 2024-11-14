def buy_product(username, products, finances):
    """ Allows an employee to buy a product """
    product_id = input("Enter product ID to buy: ")
    quantity = int(input("Enter quantity: "))
    
    if product_id not in products:
        print("Product not found.")
        return
    
    product = products[product_id]
    if quantity > product.stock:
        print("Not enough stock available.")
        return
    
    total_cost = quantity * product.price
    if total_cost > finances.balance:
        print("Insufficient funds.")
        return
    
    product.stock -= quantity
    finances.balance -= total_cost
    print(f"Purchased {quantity} of {product.name}. Total cost: {total_cost}. Remaining balance: {finances.balance}.")

def sell_product(username, products, finances):
    """ Allows an employee to sell a product """
    product_id = input("Enter product ID to sell: ")
    quantity = int(input("Enter quantity: "))
    
    if product_id not in products:
        print("Product not found.")
        return
    
    product = products[product_id]
    if quantity < 0:
        print("Quantity cannot be negative.")
        return
    
    product.stock += quantity
    total_income = quantity * product.price
    finances.balance += total_income
    print(f"Sold {quantity} of {product.name}. Total income: {total_income}. Current balance: {finances.balance}.")
