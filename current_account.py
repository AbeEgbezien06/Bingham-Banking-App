from account import Account
class CurrentAccount(Account):

    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)

current_account = CurrentAccount("987654321", "Barnabas Egbezien", 1000000)
current_account.deposit(50000)
current_account.withdraw(200000)
current_account.withdraw(1500000)  # This should work fine if balance permits
print(current_account.get_account_details())