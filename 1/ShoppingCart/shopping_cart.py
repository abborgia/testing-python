class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class ShoppingCart:

    def __init__(self):
        self.items = []


    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
        
    def contains_item(self):
        return len(self.items) > 0

    def get_item(self, item):
        return self.items[ self.items.index(item)-1 ]

    

