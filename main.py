def calculate_total(items):
    """Calculate total price of items with discount"""
    total = 0
    for item in items:
        total += item['price']
        if 'discount' in item:
            total -= item['discount']
    return total

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
    
    def add_item(self, item):
        self.items.append(item)
        self.update_total()
    
    def update_total(self):
        """Update cart total"""
        self.total = calculate_total(self.items)
        
    async def checkout(self):
        """Process checkout asynchronously"""
        try:
            result = await self.process_payment()
            self.items = []
            self.total = 0
            return result
        except PaymentError:
            return False