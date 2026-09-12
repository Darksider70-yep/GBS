class Account:
    VALID_ACCOUNT_TYPES = {"Savings", "Current"}
    MINIMUM_BALANCES = {"Savings": 500, "Current": 1000}

    def __init__(self, accountNumber, name, age, initialBalance, accountType):
        self.accountNumber = accountNumber
        self.name = name
        self.age = max(age, 18)
        self.accountType = accountType if accountType in self.VALID_ACCOUNT_TYPES else "Savings"
        self.minimumBalance = self.MINIMUM_BALANCES[self.accountType]
        self.balance = max(initialBalance, self.minimumBalance)
        self.status = "Active"
        self.pin = None

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
        if isinstance(pin, bool) or not isinstance(pin, int) or not 1000 <= pin <= 9999:
            return False
        self.pin = pin
        return True

    def verifyPin(self, pin: int) -> bool:
        return self.pin is not None and self.pin == pin

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