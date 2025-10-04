class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if enough balance exists."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Show the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
