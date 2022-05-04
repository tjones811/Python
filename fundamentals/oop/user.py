
class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount): 
        self.account_balance += amount
        print(f"{self.name} made a deposit of {amount}")
    
    def make_withdrawl(self,amount):
        self.account_balance -= amount
        print(f"{self.name} made a withdral of {amount}")

    def dsiplay_user_balace(self):
        print(f"Account balance of {self.name} is {self.account_balance}")
    
    def transfer_money(self,recipient,amount):
        self.account_balance -= amount
        # self.make_withdrawl(amount)
        recipient.account_balance += amount
        # recipient.make_deposit(amount)

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



trey.transfer_money(leo,1)
trey.dsiplay_user_balace()
leo.dsiplay_user_balace()



