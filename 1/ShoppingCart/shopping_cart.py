class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class ShoppingCart:

    def __init__(self):
        self.items = []


    def add_item(self):
        