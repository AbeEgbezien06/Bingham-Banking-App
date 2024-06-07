from account import Account
class CurrentAccount(Account):
    def __init__(self, initial_balance=0):
        super().__init__(initial_balance) 

    def __str__(self):
        return f"Available Balance: {self.get_balance()}"

current = CurrentAccount()

while True:
    action = input("Enter 'd' for deposit, 'w' for withdrawal, or 'q' to quit: ")
    if action.lower() == 'q':
        break

    try:
        if action.lower() == 'd':
            amount = float(input("Enter Amount to deposit: "))
            current.deposit(amount)
        elif action.lower() == 'w':
            amount = float(input("Enter Amount to withdraw: "))
            current.withdraw(amount)
        else:
            print("Invalid action. Please enter 'd', 'w', or 'q'.")
    except ValueError as e:
        print(f"Error: {e}")

print("Exiting program.")
