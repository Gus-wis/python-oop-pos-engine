class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.__price = price  # Hidden variable (Encapsulation)
        self.stock = stock

    # Getter for price to protect it from direct outside modification
    @property
    def price(self) -> float:
        return self.__price

    def reduce_stock(self, quantity: int) -> bool:
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

    def restock(self, quantity: int):
        if quantity > 0:
            self.stock += quantity