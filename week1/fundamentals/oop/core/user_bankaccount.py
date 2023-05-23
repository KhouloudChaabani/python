from bank_account import BankAccount
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_info(self):
        print("User:", self.name)
        self.account.display_account_info()

user3=User("john","johndolf@gmail.com")
user3.make_deposit(100)
user3.make_withdrawal(50)
user3.display_user_info()