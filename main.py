class BankAccount:
    accounts = []

    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance 
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount 
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account(self):
        print(f'Balance: {self.balance}')
        return self

    def yield_int(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account()

saving = BankAccount(.05, 900)
checking = BankAccount(.02, 800)
saving.deposit(300).deposit(500).deposit(100).withdraw(100).yield_int().display_account()
checking.deposit(500).deposit(500).deposit(300).withdraw(100).yield_int().display_account()

BankAccount.print_all_accounts()

"""
output:
Balance: 1785.0
Balance: 2040.0
Balance: 1785.0
Balance: 2040.0

"""

