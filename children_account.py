from savings_account import Account

class ChildrenAccount(Account):
    def __init__(self, account_holder, balance=0, interest_rate=0.007):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added. New balance is {self.balance}.")

    def withdraw(self, amount):
        print("Withdrawals are not allowed from a children's account.")

def main():
    print("Welcome to the Bank App")
    name = input("Enter account holder's name: ")
    account = ChildrenAccount(name)

    while True:
        print("\nMenu:")
        print("1. Deposit Money")
        print("2. Add Interest")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            account.add_interest()
        elif choice == '3':
            print(f"Current balance: {account.get_balance()}")
        elif choice == '4':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()        