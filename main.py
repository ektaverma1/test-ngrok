def calculate_total(items):
    """Calculate total price of items"""
    total = 0
    for item in items:
        total += item['price']
    return total

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)