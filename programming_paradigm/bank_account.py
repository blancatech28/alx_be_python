class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, deposit_amount):
        self.account_balance += deposit_amount
        return f"Deposited: ${deposit_amount:.2f}"

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.account_balance:
            self.account_balance -= withdraw_amount
            return f"Withdrew: ${withdraw_amount:.2f}"
        else:
            return "Insufficient funds."

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"