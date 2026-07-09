from models.product import Product
from models.user import Customer, Admin
from core.cart import ShoppingCart
from core.checkout import Order
from core.payment import EWalletPayment, BankTransferPayment

# 1. Prepare backend inventory list
store_catalog = []

# 2. Instantiate User Roles using Inheritance
admin = Admin("A01", "Pak Yudi", "yudi@umkm.com")
customer = Customer("C01", "Satria", "satria@binus.ac.id")

# 3. Admin updates catalogue data paths
kb = Product("P001", "Mechanical Keyboard", 450000.0, 5)
mouse = Product("P002", "Wireless Mouse", 180000.0, 2)

admin.add_new_product(store_catalog, kb)
admin.add_new_product(store_catalog, mouse)

print("\n--- Shopper Interaction Simulation ---")

# 4. Instantiate a user's local container using Composition
cart = ShoppingCart()

# Add items into cart (Checks product availability safely)
cart.add_item(kb, 1)
cart.add_item(mouse, 2)
# Try adding an item that exceeds current inventory limits
cart.add_item(mouse, 1) 

# 5. Build full-scale Checkout Pipeline
order1 = Order("TX-9982", customer, cart)

# Choose a payment method seamlessly using Polymorphism
payment_channel = BankTransferPayment("8839012847120")

# 6. Execute transaction lifecycle
if order1.process_checkout(payment_channel):
    # Print custom invoice layout
    order1.print_receipt()
    # Clear cart for user state cleanup
    cart.clear_cart()

# Verify that product stocks were updated cleanly inside database structures
print(f"Updated store stocks -> Keyboard: {kb.stock} left | Mouse: {mouse.stock} left")