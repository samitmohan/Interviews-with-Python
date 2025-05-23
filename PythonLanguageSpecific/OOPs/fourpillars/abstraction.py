"""
Abstraction hides complex implementation details while exposing only the essential features and functionality.
It provides a clear separation between what an object does and how it does it.

Types of Abstraction:
    Interface Abstraction: Defining contracts without implementation
    Implementation Hiding: Concealing complex internal workings
    Data Abstraction: Representing essential features without background details
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Protocol
from enum import Enum
import uuid
from datetime import datetime


# Enum for order status
class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


# Abstract base class defining payment interface
class PaymentProcessor(ABC):
    """
    Abstract base class for payment processing.
    Defines the contract that all payment processors must follow.
    """

    @abstractmethod
    def validate_payment_details(self, payment_details: dict) -> bool:
        """Validate payment information before processing."""
        pass

    @abstractmethod
    def process_payment(self, amount: float, payment_details: dict) -> dict:
        """Process the payment and return transaction details."""
        pass

    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Process a refund for a previous transaction."""
        pass

    @property
    def supported_currencies(self) -> List[str]:
        """List of supported currency codes."""
        pass

    @property
    def processor_name(self) -> str:
        """Name of the payment processor."""
        pass

    def generate_transaction_id(self) -> str:
        """Generate a unique transaction ID."""
        return f"TXN_{uuid.uuid4().hex[:12].upper()}"

    def validate_amount(self, amount: float) -> bool:
        """Common validation for payment amounts."""
        return amount > 0 and amount <= 10000  # Max $10,000 per transaction


# Concrete implementation - Credit Card Processor
class CreditCardProcessor(PaymentProcessor):
    """Credit card payment processor implementation."""

    def __init__(self):
        self._supported_currencies = ["USD", "EUR", "GBP", "CAD"]
        self._processor_name = "CreditCard Gateway v2.1"

    @property
    def supported_currencies(self) -> List[str]:
        return self._supported_currencies.copy()

    @property
    def processor_name(self) -> str:
        return self._processor_name

    def validate_payment_details(self, payment_details: dict) -> bool:
        """Validate credit card details."""
        required_fields = [
            "card_number",
            "expiry_month",
            "expiry_year",
            "cvv",
            "cardholder_name",
        ]

        # Check all required fields are present
        if not all(field in payment_details for field in required_fields):
            return False

        # Validate card number (simplified - just check length)
        card_number = payment_details["card_number"].replace(" ", "").replace("-", "")
        if not (13 <= len(card_number) <= 19 and card_number.isdigit()):
            return False

        # Validate expiry date
        try:
            month = int(payment_details["expiry_month"])
            year = int(payment_details["expiry_year"])
            if not (1 <= month <= 12) or year < datetime.now().year:
                return False
        except ValueError:
            return False

        # Validate CVV
        cvv = payment_details["cvv"]
        if not (3 <= len(cvv) <= 4 and cvv.isdigit()):
            return False

        return True

    def process_payment(self, amount: float, payment_details: dict) -> dict:
        """Process credit card payment."""
        if not self.validate_amount(amount):
            raise ValueError("Invalid payment amount")

        if not self.validate_payment_details(payment_details):
            raise ValueError("Invalid payment details")

        # Simulate payment processing
        transaction_id = self.generate_transaction_id()

        # Simulated processing logic (in reality, this would call external APIs)
        success = True  # Simplified - assume success

        return {
            "transaction_id": transaction_id,
            "status": "completed" if success else "failed",
            "amount": amount,
            "currency": "USD",
            "processor": self.processor_name,
            "timestamp": datetime.now().isoformat(),
            "card_last_four": payment_details["card_number"][-4:],
        }

    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Process credit card refund."""
        return {
            "refund_id": self.generate_transaction_id(),
            "original_transaction": transaction_id,
            "refund_amount": amount,
            "status": "completed",
            "processor": self.processor_name,
            "timestamp": datetime.now().isoformat(),
        }


# Another concrete implementation - Digital Wallet Processor
class DigitalWalletProcessor(PaymentProcessor):
    """Digital wallet payment processor implementation."""

    def __init__(self):
        self._supported_currencies = ["USD", "EUR", "BTC", "ETH"]
        self._processor_name = "DigitalWallet Pro"

    @property
    def supported_currencies(self) -> List[str]:
        return self._supported_currencies.copy()

    @property
    def processor_name(self) -> str:
        return self._processor_name

    def validate_payment_details(self, payment_details: dict) -> bool:
        """Validate digital wallet details."""
        required_fields = ["wallet_address", "wallet_type", "pin"]

        if not all(field in payment_details for field in required_fields):
            return False

        # Validate wallet address format (simplified)
        wallet_address = payment_details["wallet_address"]
        if len(wallet_address) < 26 or len(wallet_address) > 62:
            return False

        # Validate PIN
        pin = payment_details["pin"]
        if not (4 <= len(pin) <= 8 and pin.isdigit()):
            return False

        return True

    def process_payment(self, amount: float, payment_details: dict) -> dict:
        """Process digital wallet payment."""
        if not self.validate_amount(amount):
            raise ValueError("Invalid payment amount")

        if not self.validate_payment_details(payment_details):
            raise ValueError("Invalid payment details")

        transaction_id = self.generate_transaction_id()

        return {
            "transaction_id": transaction_id,
            "status": "completed",
            "amount": amount,
            "currency": "USD",
            "processor": self.processor_name,
            "timestamp": datetime.now().isoformat(),
            "wallet_type": payment_details["wallet_type"],
        }

    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Process digital wallet refund."""
        return {
            "refund_id": self.generate_transaction_id(),
            "original_transaction": transaction_id,
            "refund_amount": amount,
            "status": "completed",
            "processor": self.processor_name,
            "timestamp": datetime.now().isoformat(),
        }


# Protocol for type hinting (Python 3.8+) - another form of abstraction
class Discountable(Protocol):
    """Protocol defining interface for objects that can have discounts applied."""

    def apply_discount(self, percentage: float) -> float:
        """Apply discount and return new price."""
        ...

    def get_original_price(self) -> float:
        """Get the original price before discount."""
        ...


# High-level abstraction - Order Management System
class Order:
    """
    High-level abstraction for order management.
    Hides complex payment processing and inventory management details.
    """

    def __init__(self, customer_id: str, items: List[dict]):
        self.order_id = f"ORD_{uuid.uuid4().hex[:8].upper()}"
        self.customer_id = customer_id
        self.items = items
        self.status = OrderStatus.PENDING
        self.created_at = datetime.now()
        self.total_amount = self._calculate_total()
        self.payment_processor: Optional[PaymentProcessor] = None
        self.transaction_details: Optional[dict] = None

    def _calculate_total(self) -> float:
        """Private method to calculate order total - implementation detail hidden."""
        total = sum(item["price"] * item["quantity"] for item in self.items)
        tax = total * 0.08  # 8% tax
        return round(total + tax, 2)

    def set_payment_processor(self, processor: PaymentProcessor) -> None:
        """Set the payment processor for this order."""
        self.payment_processor = processor

    def process_payment(self, payment_details: dict) -> bool:
        """
        High-level payment processing - abstracts away processor-specific details.
        Client code doesn't need to know how different payment types work.
        """
        if not self.payment_processor:
            raise ValueError("No payment processor configured")

        if self.status != OrderStatus.PENDING:
            raise ValueError(
                f"Cannot process payment for order with status: {self.status.value}"
            )

        try:
            # Abstract payment processing - details hidden from client
            self.transaction_details = self.payment_processor.process_payment(
                self.total_amount, payment_details
            )

            if self.transaction_details["status"] == "completed":
                self.status = OrderStatus.CONFIRMED
                self._update_inventory()  # Hidden implementation detail
                self._send_confirmation_email()  # Hidden implementation detail
                return True
            else:
                return False

        except Exception as e:
            print(f"Payment processing failed: {e}")
            return False

    def _update_inventory(self) -> None:
        """Private method - inventory management abstracted away."""
        print(f"Updating inventory for order {self.order_id}")
        # Complex inventory management logic hidden here

    def _send_confirmation_email(self) -> None:
        """Private method - email sending abstracted away."""
        print(f"Sending confirmation email for order {self.order_id}")
        # Complex email sending logic hidden here

    def ship_order(self) -> bool:
        """Ship the order - abstracts shipping complexity."""
        if self.status != OrderStatus.CONFIRMED:
            return False

        # Abstract shipping process
        self._generate_shipping_label()
        self._schedule_pickup()
        self.status = OrderStatus.SHIPPED
        return True

    def _generate_shipping_label(self) -> None:
        """Hidden shipping implementation detail."""
        print(f"Generating shipping label for order {self.order_id}")

    def _schedule_pickup(self) -> None:
        """Hidden shipping implementation detail."""
        print(f"Scheduling pickup for order {self.order_id}")

    def cancel_order(self) -> bool:
        """Cancel order and process refund if necessary."""
        if self.status == OrderStatus.DELIVERED:
            return False

        if self.status in [OrderStatus.CONFIRMED, OrderStatus.SHIPPED]:
            # Process refund if payment was taken
            if self.transaction_details and self.payment_processor:
                refund_result = self.payment_processor.refund_payment(
                    self.transaction_details["transaction_id"], self.total_amount
                )
                print(f"Refund processed: {refund_result['refund_id']}")

        self.status = OrderStatus.CANCELLED
        return True

    def get_order_summary(self) -> dict:
        """Get high-level order information - implementation details abstracted."""
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "status": self.status.value,
            "total_amount": self.total_amount,
            "item_count": len(self.items),
            "created_at": self.created_at.isoformat(),
            "payment_processor": self.payment_processor.processor_name
            if self.payment_processor
            else None,
        }


# Factory pattern for creating payment processors (another abstraction)
class PaymentProcessorFactory:
    """
    Factory class that abstracts the creation of payment processors.
    Client code doesn't need to know about specific processor classes.
    """

    _processors = {
        "credit_card": CreditCardProcessor,
        "digital_wallet": DigitalWalletProcessor,
    }

    @classmethod
    def create_processor(cls, processor_type: str) -> PaymentProcessor:
        """Create a payment processor instance."""
        if processor_type not in cls._processors:
            raise ValueError(f"Unknown processor type: {processor_type}")

        return cls._processors[processor_type]()

    @classmethod
    def get_available_processors(cls) -> List[str]:
        """Get list of available processor types."""
        return list(cls._processors.keys())


# Usage example demonstrating abstraction
if __name__ == "__main__":
    print("=== Abstraction Demonstration ===\n")

    # 1. High-level order creation - complexity abstracted away
    order_items = [
        {"name": "Laptop", "price": 999.99, "quantity": 1},
        {"name": "Mouse", "price": 29.99, "quantity": 2},
        {"name": "Keyboard", "price": 79.99, "quantity": 1},
    ]

    order = Order("CUST_12345", order_items)
    print(f"Order created: {order.get_order_summary()}")

    print("\n" + "-" * 50 + "\n")

    # 2. Abstract payment processing - client doesn't need to know processor details
    print("Available payment processors:")
    for processor_type in PaymentProcessorFactory.get_available_processors():
        print(f"  - {processor_type}")

    # Create payment processor using factory (abstraction)
    cc_processor = PaymentProcessorFactory.create_processor("credit_card")
    order.set_payment_processor(cc_processor)

    # Process payment - implementation details hidden
    credit_card_details = {
        "card_number": "4532 1234 5678 9012",
        "expiry_month": "12",
        "expiry_year": "2025",
        "cvv": "123",
        "cardholder_name": "John Doe",
    }

    print("\nProcessing credit card payment...")
    if order.process_payment(credit_card_details):
        print("✅ Payment successful!")
        print(f"Order status: {order.status.value}")
    else:
        print("❌ Payment failed!")

    print("\n" + "-" * 50 + "\n")

    # 3. Demonstrate polymorphic behavior with different processors
    order2 = Order("CUST_67890", [{"name": "Book", "price": 19.99, "quantity": 3}])

    # Use different payment processor
    wallet_processor = PaymentProcessorFactory.create_processor("digital_wallet")
    order2.set_payment_processor(wallet_processor)

    wallet_details = {
        "wallet_address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
        "wallet_type": "Bitcoin",
        "pin": "1234",
    }

    print("Processing digital wallet payment...")
    if order2.process_payment(wallet_details):
        print("✅ Payment successful!")
        print(f"Order status: {order2.status.value}")

    print("\n" + "-" * 50 + "\n")

    # 4. High-level operations - complexity abstracted
    print("Shipping first order...")
    if order.ship_order():
        print("✅ Order shipped!")
        print(f"Order status: {order.status.value}")

    print("\nCancelling second order...")
    if order2.cancel_order():
        print("✅ Order cancelled and refund processed!")
        print(f"Order status: {order2.status.value}")

    print("\n" + "-" * 50 + "\n")

    # 5. Demonstrate abstraction levels
    print("Final order summaries:")
    print("Order 1:", order.get_order_summary())
    print("Order 2:", order2.get_order_summary())

    print("\n=== Abstraction Benefits Demonstrated ===")
    print("✅ Client code doesn't need to know payment processor internals")
    print("✅ Order management complexity is hidden behind simple methods")
    print("✅ Different payment processors can be used interchangeably")
    print("✅ Implementation details can change without affecting client code")
    print("✅ Factory pattern abstracts object creation complexity")
