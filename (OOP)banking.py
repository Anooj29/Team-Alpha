class BankAccount:
    def __init__(self, account_num, bal):
        self.account_number = account_num
        self.balance = bal
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    
    def get_balance(self):
        return self.balance

account = BankAccount("12345", 1000)

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
        print("Deposit successful.\n")
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
        print()
    elif choice == '3':
        print("Current Balance:", account.get_balance())
        print()
    elif choice == '4':
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a valid option.\n")
