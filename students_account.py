from account import Account
class StudentAccount(Account):
    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)
        self._withdrawal_limit = 2000
        self._deposit_limit = 50000

    def deposit(self, amount):
        if amount > self._deposit_limit:
            print(f"Cannot deposit more than {self._deposit_limit} at a time.")
        elif amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}. New balance: {self._balance}")
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



student_account = StudentAccount("556677889", "Otuno  David", 30000)
student_account.deposit(60000)  # Should show an error due to the deposit limit
student_account.deposit(40000)
student_account.withdraw(2500)  # Should show an error due to the withdrawal limit
student_account.withdraw(1500)
print(student_account.get_account_details())