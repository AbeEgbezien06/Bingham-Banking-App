class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self._balance

    def get_account_details(self):
        return {
            "Account Number": self._account_number,
            "Account Holder": self._account_holder,
            "Balance": self._balance
        }