from Activity_3.AccountEnhanced import Account


def create_account() -> Account:
    account_number = input("Enter your account number: ")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    initial_balance = float(input("Enter your initial balance: "))
    account_type = input("Enter your account type (Savings/Current): ")
    return Account(account_number, name, age, initial_balance, account_type)


accounts: list[Account] = []
current_account: Account | None = None

print("An enhanced account class with validation, status management, and PIN protection.\n")

while True:
    print("=====================================\nENHANCED ACCOUNT TEST\n=====================================\n")
    print(
        "Features Available:\n"
        "1. Create Account\n"
        "2. Set PIN\n"
        "3. Deposit Money\n"
        "4. Withdraw Money\n"
        "5. Check Account\n"
        "6. Close Account\n"
        "7. Reopen Account\n"
        "8. View All Accounts\n"
        "9. Exit\n"
    )

    try:
        choice = int(input("Choose an option (1-9): "))
    except ValueError:
        print("\nPlease enter a number from 1 to 9.\n")
        continue

    if choice == 1:
        current_account = create_account()
        accounts.append(current_account)
        print("\nAccount created successfully.\n")
    elif choice == 2:
        if current_account is None:
            print("\nPlease create an account first.\n")
            continue
        pin = int(input("Enter a 4-digit PIN: "))
        print("\nPIN set successfully.\n" if current_account.setPin(pin) else "\nInvalid PIN.\n")
    elif choice == 3:
        if current_account is None:
            print("\nPlease create an account first.\n")
            continue
        amount = float(input("Enter the amount to deposit: "))
        print("\nDeposit successful.\n" if current_account.deposit(amount) else "\nDeposit failed.\n")
    elif choice == 4:
        if current_account is None:
            print("\nPlease create an account first.\n")
            continue
        amount = float(input("Enter the amount to withdraw: "))
        pin = int(input("Enter your PIN: "))
        print("\nWithdrawal successful.\n" if current_account.withdraw(amount, pin) else "\nWithdrawal failed.\n")
    elif choice == 5:
        if current_account is None:
            print("\nPlease create an account first.\n")
            continue
        print(
            f"\nAccount: {current_account.accountNumber}\n"
            f"Name: {current_account.name}\n"
            f"Age: {current_account.age}\n"
            f"Type: {current_account.accountType}\n"
            f"Balance: {current_account.balance}\n"
            f"Status: {current_account.status}\n"
            f"PIN set: {current_account.hasPin()}\n"
        )
    elif choice == 6:
        if current_account is None:
            print("\nPlease create an account first.\n")
            continue
        print("\nAccount closed.\n" if current_account.closeAccount() else "\nAccount is already closed.\n")
    elif choice == 7:
        if current_account is None:
            print("\nPlease create an account first.\n")
            continue
        print("\nAccount reopened.\n" if current_account.reopenAccount() else "\nAccount is already active.\n")
    elif choice == 8:
        print("\nAll Accounts:\n")
        for account in accounts:
            print(f"{account.accountNumber}: {account.name}, {account.balance}, {account.status}")
    elif choice == 9:
        break
    else:
        print("\nPlease choose an option from 1 to 9.\n")

print("\nThank you for using Enhanced Account Test.\n")
