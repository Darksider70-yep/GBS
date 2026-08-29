class account:
    no_of_accounts = 0
    def __init__(self, ID, name, age, AccountType, Balance, Status):
        self.ID = ID     
        self.name = name 
        self.age = age
        self.AccountType = AccountType
        self.Balance = Balance
        self.Status = Status
        account.no_of_accounts += 1

    def get_balance(self) -> float:
        return float(self.Balance)
    def get_status(self) -> str:
        return str(self.Status) 
    def deposit(self, amount: float) -> None:
        self.Balance += amount
    def withdraw(self, amount: float) -> None:
        if amount > self.Balance:
            print("Insufficient balance!")
        else:
            self.Balance -= amount  
    def __str__(self) -> str:
        return f"Account ID: {self.ID}\nName: {self.name}\nAge: {self.age}\nAccount Type: {self.AccountType}\nBalance: {self.Balance}\nStatus: {self.Status}"
    def set_status(self, status: str) -> None:
        self.Status = status
    def set_balance(self, balance: float) -> None:
        self.Balance = balance
    def set_account_type(self, account_type: str) -> None:
        self.AccountType = account_type
    def set_name(self, name: str) -> None:
        self.name = name
    def set_age(self, age: int) -> None:
        self.age = age


print("A simple account class for the global Digital bank system.\nThis is a bare bone implementation with minimal functionality.\n\nA simple account class with basic deposit and withdraw functionality.\n")

new_account: account | None = None

while True:
    print("=====================================\nGLOBAL DIGITAL BANK - ACCOUNT TEST\n=====================================\n")
    print("Features Available:\n1. Create Account\n2. Deposit Money\n3. Withdraw Money\n4. Check Balance\n5. Check Account Status\n6. Create Another Account\n7. View All Accounts\n8. Exit\n")

    try:
        ans = int(input("Choose an option (1-8): "))
    except ValueError:
        print("\nPlease enter a number from 1 to 8.\n")
        continue

    match ans:
        case 1:
            print("\nCreate Account\n")
            ID = input("Enter your ID: ")
            name = input("Enter your name: ")
            AccountType = input("Enter your account type (Savings/Current): ")
            Balance = float(input("Enter your initial balance: "))
            Status = input("Enter your account status (Active/Inactive): ")
            age = int(input("Enter your age: "))
            new_account = account(ID, name, age, AccountType, Balance, Status)
            print("\nAccount created successfully!\n")
            no_of_accounts = account.no_of_accounts
            print(f"\nYou have created {no_of_accounts} account(s) so far.\n")
        case 2:
            if new_account is None:
                print("\nPlease create an account first.\n")
                continue
            amount = float(input("Enter the amount to deposit: "))
            new_account.deposit(amount)
            print(f"\nAmount deposited successfully! New balance: {new_account.get_balance()}\n")
        case 3:
            if new_account is None:
                print("\nPlease create an account first.\n")
                continue
            amount = float(input("Enter the amount to withdraw: "))
            new_account.withdraw(amount)
            print(f"\nAmount withdrawn successfully! New balance: {new_account.get_balance()}\n")
        case 4:
            if new_account is None:
                print("\nPlease create an account first.\n")
                continue
            print(f"\nYour current balance is: {new_account.get_balance()}\n")
        case 5:
            if new_account is None:
                print("\nPlease create an account first.\n")
                continue
            print(f"\nYour account status is: {new_account.get_status()}\n")
        case 6:
            new_account = None
            ID = input("Enter your ID: ")
            name = input("Enter your name: ")
            AccountType = input("Enter your account type (Savings/Current): ")
            Balance = float(input("Enter your initial balance: "))
            Status = input("Enter your account status (Active/Inactive): ")
            age = int(input("Enter your age: "))
            new_account = account(ID, name, age, AccountType, Balance, Status)
            no_of_accounts = account.no_of_accounts
            print(f"\nYou have created {no_of_accounts} account(s) so far.\n")
        case 7:
            print("\nAll Accounts:\n")
            for acc in account.all_accounts:
                print(f"ID: {acc.get_id()}, Name: {acc.get_name()}, Balance: {acc.get_balance()}, Status: {acc.get_status()}, Account Type: {acc.get_account_type()}")
        case 8:
            break
        case _:
            print("\nPlease choose an option from 1 to 8.\n")

print("\nThank you for using Global Digital Bank.\n")
