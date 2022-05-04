class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount): 
        self.account_balance += amount
        print(f"{self.name} made a deposit of {amount}")
        return self
    
    def make_withdrawl(self,amount):
        self.account_balance -= amount
        print(f"{self.name} made a withdral of {amount}")
        return self

    def dsiplay_user_balace(self):
        print(f"Account balance of {self.name} is {self.account_balance}")
        return self
    
    def transfer_money(self,recipient,amount):
        # self.account_balance -= amount
        self.make_withdrawl(amount)
        # recipient.account_balance += amount
        recipient.make_deposit(amount)
        return self

leo = User("Leo","leo-email.com")
trey = User("Trey","trey-email.com")
levi = User("Levi","levi-email.com")

leo.make_deposit(5000).make_deposit(5000).make_deposit(3000).make_withdrawl(2000).dsiplay_user_balace()

trey.make_deposit(20000).make_deposit(20000).make_withdrawl(100).make_withdrawl(5000).dsiplay_user_balace()

levi.make_deposit(700).make_withdrawl(200).make_withdrawl(300).make_withdrawl(10).dsiplay_user_balace()



trey.transfer_money(leo,1).dsiplay_user_balace()
leo.dsiplay_user_balace()