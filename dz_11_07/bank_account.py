class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value    

    def add_interest(self):
        self.balance += self.balance / 100 * self.interest_rate

    def is_negative(self):
        if self.balance <= 0:
            return True
        else:
            return False
        

if __name__ == "__main__":
    account = BankAccount(0, 10)
    account.deposit(10)
    print(account.balance)
    account.withdraw(110)
    print(account.balance)
    print(account.is_negative())
    account.deposit(1000)
    print(account.is_negative())