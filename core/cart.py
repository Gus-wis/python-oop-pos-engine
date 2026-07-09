from models.product import Product

class ShoppingCart:
    def __init__(self):
        # Composition: The cart holds a list of Product objects and their quantities
        self.items = {}  # Format: {Product_Object: quantity}

    def add_item(self, product: Product, quantity: int = 1) -> bool:
        if quantity <= 0:
            print("[CART ERROR] Quantity must be greater than zero.")
            return False
        
        # Safety check: Ensure the store actually has enough stock before adding to cart
        if product.stock >= quantity:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            print(f"[CART] Added {quantity}x '{product.name}' to your cart.")
            return True
        else:
            print(f"[CART ERROR] Cannot add '{product.name}'. Only {product.stock} items available.")
            return False

    def remove_item(self, product: Product):
        if product in self.items:
            del self.items[product]
            print(f"[CART] Removed '{product.name}' completely from your cart.")

    def calculate_total(self) -> float:
        # Uses the Product's encapsulated price property to sum up the total bill
        return sum(product.price * qty for product, qty in self.items.items())

    def clear_cart(self):
        self.items.clear()