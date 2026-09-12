class Account:
    no_of_accounts = 0
    VALID_ACCOUNT_TYPES = {"Savings", "Current"}
    MINIMUM_BALANCES = {"Savings": 500, "Current": 1000}

    def __init__(self, accountNumber, name, age, initialBalance, accountType):
        self.accountNumber = accountNumber
        Account.no_of_accounts += 1
        self.name = name
        self.age = max(age, 18)
        self.accountType = accountType if accountType in self.VALID_ACCOUNT_TYPES else "Savings"
        self.minimumBalance = self.MINIMUM_BALANCES[self.accountType]
        self.balance = max(initialBalance, self.minimumBalance)
        self.status = "Active"
        self.pin = None

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
    
    accounts = []
        
    @staticmethod
    def all_accounts() -> list:
        return Account.accounts
        
    @staticmethod
    def add_account(new_account) -> None:
        Account.accounts.append(new_account)


    def closeAccount(self) -> bool:
        if self.status == "Inactive":
            return False
        self.status = "Inactive"
        return True

    def reopenAccount(self) -> bool:
        if self.status == "Active":
            return False
        self.status = "Active"
        return True

    def setPin(self, pin: int) -> bool:
        if isinstance(pin, bool) or not isinstance(pin, int) or not (1000 <= pin <= 9999):
            return False
        self.pin = pin
        return True

    def verifyPin(self, pin: int) -> bool:
        return self.pin == pin

    def hasPin(self) -> bool:
        return self.pin is not None

    def deposit(self, amount) -> bool:
        if self.status == "Inactive" or amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount, pin) -> bool:
        if self.status == "Inactive" or not self.verifyPin(pin):
            return False
        if amount <= 0 or self.balance - amount < self.minimumBalance:
            return False
        self.balance -= amount
        return True