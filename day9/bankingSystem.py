class ATM:
    def __init__(self):
        self.balance = 1000  # Initial balance in the ATM

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Your new balance is: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive number.")
        elif amount > self.balance:
            print("Insufficient funds! Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Your new balance is: ${self.balance}")

    def run(self):
        print("Welcome to the ATM system!")
        while True:
            print("\nSelect an option:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                try:
                    amount = float(input("Enter deposit amount: $"))
                    self.deposit(amount)
                except ValueError:
                    print("Please enter a valid number for deposit.")
            elif choice == '3':
                try:
                    amount = float(input("Enter withdrawal amount: $"))
                    self.withdraw(amount)
                except ValueError:
                    print("Please enter a valid number for withdrawal.")
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
