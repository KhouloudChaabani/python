class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        return self
     
    def withdraw(self, amount): 
         if self.balance >= amount:
            self.balance -= amount
         else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
         return self

    def display_account_info(self):  
        print("Balance:$" + str(self.balance))

    def yield_interest(self):
        if self.balance > 0:
            interest=self.balance*self.interest_rate
            self.balance += interest

acc1 = BankAccount(0.1,0)
acc1.deposit(100).deposit(200).deposit(120)
acc1.display_account_info()
acc1.withdraw(50)
acc1.display_account_info()
acc1.yield_interest()
acc1.display_account_info()
acc2 = BankAccount(0.2,0)
acc1.deposit(100).deposit(300)
acc1.display_account_info()
acc1.withdraw(50).withdraw(40).withdraw(100).withdraw(50)
acc1.display_account_info()
acc1.yield_interest()
acc1.display_account_info()

