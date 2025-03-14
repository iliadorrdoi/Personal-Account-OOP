from datetime import datetime

class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.timestamp} | {self.transaction_type}: {self.amount:.2f}"

class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            transaction = Amount(amount, 'DEPOSIT')
            self.transactions.append(transaction)
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            transaction = Amount(amount, 'WITHDRAWAL')
            self.transactions.append(transaction)
            self.balance -= amount
            print(f"Withdrawn {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def print_transaction_history(self):
        print(f"Transaction history for {self.account_holder} (Account: {self.account_number}):")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account {self.account_number}: {self.account_holder}, Balance: {self.balance:.2f}"

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self

# Test scenario
if __name__ == "__main__":
    account = PersonalAccount(123456, "John Doe")
    account.deposit(500)
    account.withdraw(200)
    print(f"Current balance: {account.get_balance():.2f}")
    account.print_transaction_history()
