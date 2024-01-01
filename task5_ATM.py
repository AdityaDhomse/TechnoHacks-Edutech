class ATM:
    def __init__(self, balance = 0):
        self.balance = balance

    def check_balance(self):
        return f"Your balance is {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"\n{amount} deposited.\nYour new balance is {self.balance}."

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"\n{amount} withdrawn.\nYour new balance is {self.balance}."
        else:
            return "Insufficient funds. Transaction canceled."

atm = ATM()
while True:

    print("\n------ATM Menu------")
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("\n--------------------")

    choice = input("\nEnter your choice: ")

    print("\n--------------------")

    if choice == "1":
        print(atm.check_balance())

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        print(atm.deposit(amount))

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        print(atm.withdraw(amount))

    elif choice == "4":
        print("\nThank you for using the ATM. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a valid option.")

    print("\n--------------------")