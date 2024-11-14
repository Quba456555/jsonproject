import json

class Finance:
    def __init__(self, balance):
        self.balance = balance

    @staticmethod
    def from_json(data):
        return Finance(data['balance'])

    def to_json(self):
        return {
            'balance': self.balance
        }

def load_finances(filename):
    """ Load finance data from a JSON file """
    with open(filename, 'r') as file:
        data = json.load(file)
        return Finance.from_json(data)

def save_finances(filename, finance):
    """ Save finance data to a JSON file """
    with open(filename, 'w') as file:
        json.dump(finance.to_json(), file, indent=4)
