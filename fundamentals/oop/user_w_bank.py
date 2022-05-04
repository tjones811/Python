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


class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(.01)
    
    def make_deposit(self, amount): 
        self.account.deposit(amount)
        print(f"{self.name} made a deposit of {amount}")
    
    def make_withdrawl(self,amount):
        self.account.withdraw(amount)
        print(f"{self.name} made a withdral of {amount}")

    def dsiplay_user_balace(self):
        self.account.display_account_info()
    
    

leo = User("Leo","leo-email.com")
trey = User("Trey","trey-email.com")
levi = User("Levi","levi-email.com")

leo.make_deposit(5000)
leo.make_deposit(5000)
leo.make_deposit(3000)
leo.make_withdrawl(2000)
leo.dsiplay_user_balace()

trey.make_deposit(20000)
trey.make_deposit(20000)
trey.make_withdrawl(100)
trey.make_withdrawl(5000)
trey.dsiplay_user_balace()

levi.make_deposit(700)
levi.make_withdrawl(200)
levi.make_withdrawl(300)
levi.make_withdrawl(10)
levi.dsiplay_user_balace()








