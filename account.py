class account:
    def __init__(self, ID, name, AccountType, Balance, Status):
        self.ID = ID     
        self.name = name 
        self.AccountType = AccountType
        self.Balance = Balance
        self.Status = Status

print("A simple account class for the global Digital bank system.\nThis is a bare bone implementation with minimal functionality.\n\nA simple account class with basic deposit and withdraw functionality.\n")

new_account: account | None = None

while True:
    print("=====================================\nGLOBAL DIGITAL BANK - ACCOUNT TEST\n=====================================\n")
    print("Features Available:\n1. Create Account\n2. Deposit Money\n3. Withdraw Money\n4. Check Balance\n5. Check Account Status\n6. Exit\n")

    try:
        ans = int(input("Choose an option (1-6): "))
    except ValueError:
        print("\nPlease enter a number from 1 to 6.\n")
        continue

    match ans:
        case 1:
            print("\nCreate Account\n")
            ID = input("Enter your ID: ")
            name = input("Enter your name: ")
            AccountType = input("Enter your account type (Savings/Current): ")
            Balance = float(input("Enter your initial balance: "))
            Status = input("Enter your account status (Active/Inactive): ")
            new_account = account(ID, name, AccountType, Balance, Status)
            print("\nAccount created successfully!\n")
        case 2:
            if new_account is None:
                print("\nPlease create an account first.\n")
                continue
            amount = float(input("Enter the amount to deposit: "))
            new_account.Balance += amount
            print(f"\nAmount deposited successfully! New balance: {new_account.Balance}\n")
        case 3:
            if new_account is None:
                print("\nPlease create an account first.\n")
                continue
            amount = float(input("Enter the amount to withdraw: "))
            if amount > new_account.Balance:
                print("\nInsufficient balance!\n")
            else:
                new_account.Balance -= amount
                print(f"\nAmount withdrawn successfully! New balance: {new_account.Balance}\n")
        case 4:
            if new_account is None:
                print("\nPlease create an account first.\n")
                continue
            print(f"\nYour current balance is: {new_account.Balance}\n")
        case 5:
            if new_account is None:
                print("\nPlease create an account first.\n")
                continue
            print(f"\nYour account status is: {new_account.Status}\n")
        case 6:
            break
        case _:
            print("\nPlease choose an option from 1 to 6.\n")

print("\nThank you for using Global Digital Bank.\n")
