from models.product import Product

class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def get_role(self) -> str:
        return "Generic User"


# Customer inherits from User
class Customer(User):
    def __init__(self, user_id: str, name: str, email: str):
        super().__init__(user_id, name, email)  # Triggers the parent constructor
        self.purchase_history = []

    def get_role(self) -> str:
        return "Customer"


# Admin inherits from User
class Admin(User):
    def __init__(self, user_id: str, name: str, email: str):
        super().__init__(user_id, name, email)
        
    def get_role(self) -> str:
        return "Admin"

    # Unique Admin behavior
    def add_new_product(self, catalog: list, product: Product):
        catalog.append(product)
        print(f"[ADMIN ACTION] Product '{product.name}' added to inventory.")