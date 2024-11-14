import json

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    @classmethod
    def from_json(cls, data):
        return cls(data['product_id'], data['name'], data['price'], data['stock'])

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }

def load_products(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return {product['product_id']: Product.from_json(product) for product in data}

def save_products(filename, products):
    with open(filename, 'w') as file:
        json.dump([product.to_dict() for product in products.values()], file, indent=4)
