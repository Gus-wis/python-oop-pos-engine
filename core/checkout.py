import datetime
from models.user import Customer
from core.cart import ShoppingCart
from core.payment import PaymentProcessor

class Order:
    def __init__(self, order_id: str, customer: Customer, cart: ShoppingCart):
        self.order_id = order_id
        self.customer = customer
        # Snapshots the current total bill from the cart contents
        self.total_amount = cart.calculate_total()
        # Copies items over to build a receipt record
        self.items_ordered = dict(cart.items)
        self.order_date = datetime.datetime.now()
        self.is_paid = False

    def process_checkout(self, payment_method: PaymentProcessor) -> bool:
        if not self.items_ordered:
            print("[CHECKOUT ERROR] Cannot checkout an empty order.")
            return False

        print(f"\nProcessing Order #{self.order_id} for {self.customer.name}...")
        print(f"Grand Total: Rp{self.total_amount:,.2f}")

        # 1. Final verification: Check and deduct stock safely using encapsulation rules
        for product, qty in self.items_ordered.items():
            if product.stock < qty:
                print(f"[CHECKOUT FAILED] '{product.name}' ran out of stock during checkout!")
                return False

        # 2. Polymorphic execution: Process payment regardless of method details
        payment_success = payment_method.process_payment(self.total_amount)

        if payment_success:
            # Deduct inventory items since payment cleared safely
            for product, qty in self.items_ordered.items():
                product.reduce_stock(qty)
            
            self.is_paid = True
            # Log it to customer profile
            self.customer.purchase_history.append(self)
            print(f"Order #{self.order_id} successfully finalized!")
            return True
        else:
            print("[CHECKOUT FAILED] Payment transaction was rejected.")
            return False

    def print_receipt(self):
        print("\n========================= RECEIPT =========================")
        print(f"Order ID: {self.order_id} | Date: {self.order_date.strftime('%Y-%m-%d %H:%M')}")
        print(f"Customer: {self.customer.name} ({self.customer.email})")
        print("-----------------------------------------------------------")
        for product, qty in self.items_ordered.items():
            subtotal = product.price * qty
            print(f"- {product.name:<25} {qty}x @ Rp{product.price:<10:,.0f} = Rp{subtotal:,.2f}")
        print("-----------------------------------------------------------")
        print(f"TOTAL PAID VIA {type(self.customer.purchase_history[-1].is_paid).__name__ if self.is_paid else 'UNPAID'}: Rp{self.total_amount:,.2f}")
        print("===========================================================\n")