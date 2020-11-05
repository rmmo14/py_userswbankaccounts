class User:
    def __init__(self, username, email_address, int_rate = 0, balance = 0):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate, balance)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
        # print(self.account.balance)
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.display_account_info()
        return self
    def transfer_money(self, other_user, amount):
        self.account.account -= amount
        other_user.account.account += amount
        print('User 1: ', self.name, ', Balance: ', self.account.account)
        print('User 2: ', other_user.name, ', Balance: ', other_user.account.account)
      
class BankAccount(User):
    def __init__(self, int_rate, balance):
        self.interest = int_rate/100
        self.account = balance
    def deposit(self, amount):
        self.account += amount
        return self
    def withdraw(self, amount):
        if self.account > amount:
            self.account -= amount
        else:
            print ("Insufficient funds, charging a $5 fee")
            self.account -= (amount + 5)
        return self
    def display_account_info(self):
        print(f"balance: {self.account}")
        return self
    def yield_interest(self):
        if self.account > 0:
            self.account = self.interest * self.account + self.account
            # print(self.account)
        return self


guido = User("Guido van Rossum", "guido@python.com",int_rate = 10, balance = 4)
johni = User("Johni Than", "johnithan@python.com")

# print(guido.make_deposit(100).make_deposit(75).make_deposit(215).make_withdrawl(85).account.yield_interest())

guido.make_deposit(100).make_deposit(75).make_deposit(215).make_withdrawl(85).account.yield_interest().display_user_balance()
johni.make_deposit(185).make_deposit(315).make_withdrawl(75).make_withdrawl(110).make_withdrawl(245).make_withdrawl(60).account.yield_interest().display_user_balance()

# guido.account.deposit(100).deposit(75).deposit(215).withdraw(85).yield_interest().display_account_info()
# johni.account.deposit(185).deposit(315).withdraw(75).withdraw(110).withdraw(415).withdraw(60).yield_interest().display_account_info()