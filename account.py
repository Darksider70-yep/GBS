class account:
    def __init__(self, ID, name, AccountType, Balance, Status):
        self.ID = ID     
        self.name = name 
        self.AccountType = AccountType
        self.Balance = Balance
        self.Status = Status

Obj = account(123456, "John Doe", "Savings", 1000.00, "Active")

print("A simple account class for the global Digital bank system.\nThis is a bare bone implementation with minimal functionality.\n\nA simple account class with basic deposit and withdraw functionality.\n\nExpected Output")
print("=====================================\nGLOBAL DIGITAL BANK - ACCOUNT TEST\n=====================================\n")

print("Account ID:", Obj.ID)
print("Account Name:", Obj.name)
print("Account Type:", Obj.AccountType)
print("Account Balance:", Obj.Balance)
print("Account Status:", Obj.Status)
print

