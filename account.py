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

    accounts = []
    
    @staticmethod
    def all_accounts() -> list:
        return account.accounts
    
    @staticmethod
    def add_account(new_account) -> None:
        account.accounts.append(new_account)
    