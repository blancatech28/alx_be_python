class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self,deposit_amount):
        self.account_balance += deposit_amount
        return f"Deposited: ${self.account_balance}"

    def withdraw(self,withdraw_amount):
        if withdraw_amount <= self.account_balance:
            self.account_balance-= withdraw_amount
            print(f"Withdrew: ${withdraw_amount}")
            return True

        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        return f"Current Balance: ${self.account_balance}"


bank_account = BankAccount()
print(bank_account.display_balance())





