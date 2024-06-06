from account import Account


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)
        self._interest_rate = 0.005
        self._withdrawal_limit = 700000

    def deposit(self, amount):
        if amount > 0:
            interest = amount * self._interest_rate
            self._balance += amount + interest
            print(f"Deposited: {amount}. Interest earned: {interest}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self._withdrawal_limit:
            print(f"Cannot withdraw more than {self._withdrawal_limit} at a time.")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
            print(f"Withdrew: {amount}. New balance: {self._balance}")


savings_account = SavingsAccount("123456789", "Barnabas Egbezien", 500000)
savings_account.deposit(10000)
savings_account.withdraw(200000)
savings_account.withdraw(800000)  # Should show an error due to the withdrawal limit
print(savings_account.get_account_details())