class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
        # your code here

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
        # your code here

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
        # your code here


account1 = BankAccount(0.01, 100).deposit(10).deposit(25).deposit(5).withdraw(
    30).yield_interest().display_account_info()

account2 = BankAccount(0.02, 50).deposit(100).deposit(75).withdraw(25).withdraw(25).withdraw(
    25).withdraw(25).yield_interest().display_account_info()
