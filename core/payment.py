from abc import ABC, abstractmethod

# The abstract blueprint
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass


# First polymorphic child implementation
class EWalletPayment(PaymentProcessor):
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def process_payment(self, amount: float) -> bool:
        print(f"Connecting to E-Wallet gateway for account {self.phone_number}...")
        print(f"Successfully deducted Rp{amount:,.2f} via digital wallet.")
        return True


# Second polymorphic child implementation
class BankTransferPayment(PaymentProcessor):
    def __init__(self, virtual_account_num: str):
        self.va_number = virtual_account_num

    def process_payment(self, amount: float) -> bool:
        print(f"Validating Virtual Account {self.va_number}...")
        print(f"Received Bank Transfer payment of Rp{amount:,.2f}.")
        return True