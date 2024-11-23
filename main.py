def calculate_total(items):
    """Calculate total price of items with discount"""
    total = 0
    # Added a comment to trigger change
    # Iterate through items and calculate total
    for item in items:
        total += item['price']
        if 'discount' in item:
            total -= item['discount']
    return total

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0  # Added comment here
    
    def add_item(self, item):
        # Added validation
        if not isinstance(item, dict):
            raise ValueError("Item must be a dictionary")
        self.items.append(item)
        self.update_total()