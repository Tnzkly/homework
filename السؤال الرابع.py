class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance
bank_account = BankAccount("123456789", "sidra")
bank_account.deposit(1000)
print("Balance after deposit: $", bank_account.get_balance())
bank_account.withdraw(500)
print("Balance after withdrawal: $", bank_account.get_balance())

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
    def print(self):
        print("Balance: $", self.get_balance())
        print("Interest Rate: ", self.interest_rate)
savings_account = SavingsAccount("987654321", "sidra", 0.05)
savings_account.deposit(2000)
print("Balance before applying interest: $", savings_account.get_balance())
savings_account.apply_interest()
print("Balance after applying interest: $", savings_account.get_balance())
savings_account.print()

