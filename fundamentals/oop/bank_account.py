
class BankAccount:
    
    def __init__(self,int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance >0:
            self.balance += self.int_rate*self.balance
        else:
            print("No funds.")
        
        return self
    

account21 = BankAccount(.5,100)
account811 = BankAccount(.5)

account21.deposit(100).deposit(100).deposit(100).yield_interest().display_account_info()
account811.deposit(1000).deposit(1000).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()