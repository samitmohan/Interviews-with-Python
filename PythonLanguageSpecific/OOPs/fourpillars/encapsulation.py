"""
Encapsulation is the bundling of data (attributes) and methods that operate on that data within a single unit (class)
while restricting direct access to some of the object's components.

Data Hiding: private/protected attributes,
Controlled Access: getter/setter/property,
Interface Design : exposing only what's necessary for external use
"""


class BankAccount:
    """Demonstrates Encapsualtion principles"""

    def __init__(self, account_number: str, initial_balance: float = 0.0) -> None:
        # public
        self.account_num = account_number
        # protected
        self._account_type = "Savings"
        # private
        self.__balance = initial_balance
        self.__transaction_history = []
        if initial_balance < 0:
            raise ValueError("Initial balance can't be negative")

    def deposit(self, amount: float) -> None:
        """Deposits money into account"""
        if amount <= 0:
            raise ValueError("Deposit can't be negative")
        self.__balance += amount
        self.__add_transaction(f"Deposit : ${amount:.2f}")
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Can't withdraw")
        if amount > self.__balance:
            print("Insufficient Funds")

        self.__balance -= amount
        self.__add_transaction(f"Withdraw: - ${amount:.2f}")
        print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True

    # private methods for add transaction
    def __add_transaction(self, transaction: str) -> None:
        """Private method to record transactions"""
        from datetime import datetime

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transaction_history.append(f"[{timestamp}] {transaction}")

    # public method that use private data
    def get_transaction_history(self, n_last: int = 5) -> list:
        return self.__transaction_history[-n_last:]

    def __str__(self) -> str:
        return f"BankAccount({self.account_num}): ${self.__balance:2f}"

    # getters and setters for private variables
    # Property for controlled access to balance (read-only)
    @property
    def balance(self) -> int:
        return self.__balance

    @property
    def account_type(self) -> str:
        return self._account_type

    @account_type.setter
    def account_type(self, val: str) -> None:
        valid_types = ["Savings", "Business", "Checking"]
        if val not in valid_types:
            raise ValueError(f"Account type must be one of: {valid_types}")
        self._account_type = val


if __name__ == "__main__":
    account = BankAccount("ACC-12345", 1000.0)

    # Public interface usage
    print(f"Initial balance: ${account.balance:.2f}")  # Property access
    account.deposit(500)
    account.withdraw(200)

    # Controlled access through properties
    account.account_type = "Checking"  # Uses setter with validation
    print(f"Account type: {account.account_type}")

    # This would raise an error due to validation:
    # account.account_type = "InvalidType"

    # Accessing transaction history
    print("Recent transactions:")
    for transaction in account.get_transaction_history():
        print(f"  {transaction}")

    print("\n--- Demonstrating Encapsulation Protection ---")

    # Direct access to private attributes is prevented
    print(f"Balance through property: ${account.balance:.2f}")

    # This would cause an AttributeError:
    # print(account.__balance)  # AttributeError

    # Name mangling makes it harder to access (but not impossible)
    # print(account._BankAccount__balance)  # This would work but breaks encapsulation
