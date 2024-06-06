# main.py
from savings_account import SavingsAccount
from children_account import ChildrenAccount
from students_account import StudentAccount
from current_account import CurrentAccount

def main():
    print("Welcome to the Bank App")

    accounts = {}

    while True:
        print("\nMain Menu:")
        print("1. Create Savings Account")
        print("2. Create Children Account")
        print("3. Create Student Account")
        print("4. Create Current Account")
        print("5. Interact with Account")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder's name: ")
            account = SavingsAccount(account_number, account_holder)
            accounts[account_number] = account
            print(f"Savings Account created for {account_holder}")
        elif choice == '2':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder's name: ")
            account = ChildrenAccount(account_number, account_holder)
            accounts[account_number] = account
            print(f"Children Account created for {account_holder}")
        elif choice == '3':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder's name: ")
            account = StudentAccount(account_number, account_holder)
            accounts[account_number] = account
            print(f"Student Account created for {account_holder}")
        elif choice == '4':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder's name: ")
            account = CurrentAccount(account_number, account_holder)
            accounts[account_number] = account
            print(f"Current Account created for {account_holder}")
        elif choice == '5':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                if isinstance(account, SavingsAccount):
                    interact_with_savings_account(account)
                elif isinstance(account, ChildrenAccount):
                    interact_with_children_account(account)
                elif isinstance(account, StudentAccount):
                    interact_with_student_account(account)
                elif isinstance(account, CurrentAccount):
                    interact_with_current_account(account)
            else:
                print("Account not found.")
        elif choice == '6':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def interact_with_savings_account(account):
    while True:
        print("\nSavings Account Menu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Current balance: {account.get_balance()}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def interact_with_children_account(account):
    while True:
        print("\nChildren Account Menu:")
        print("1. Deposit Money")
        print("2. Add Interest")
        print("3. Check Balance")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            account.add_interest()
        elif choice == '3':
            print(f"Current balance: {account.get_balance()}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def interact_with_student_account(account):
    while True:
        print("\nStudent Account Menu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Current balance: {account.get_balance()}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def interact_with_current_account(account):
    while True:
        print("\nCurrent Account Menu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Current balance: {account.get_balance()}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


