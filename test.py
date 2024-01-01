class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"${amount} deposited. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"${amount} withdrawn. Your new balance is ${self.balance}"
        else:
            return "Insufficient funds. Transaction canceled."

# Main function to interact with the ATM
def main():
    atm = ATM()  # Initialize ATM with zero balance
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter amount to deposit: $"))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: $"))
            print(atm.withdraw(amount))
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
