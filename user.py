
class User:

    def __init__(self,name,) :
        self.name = name
        self.amouth = 0

    def make_deposit(self,amouth):
        self.amouth += amouth
        return self

    def make_withdrawal(self,amouth):
        self.amouth -= amouth
        return self

    def display_user_balance(self):
        print(F"User: {self.name}, Balance: {self.amouth}")
        return self

    def transfer_money(self,amouth,user1):
        self.amouth -= amouth
        user1.amouth += amouth
        return self

mike = User("Mike")
goku = User("Goku")
vegeta = User("Vegeta")

mike.make_deposit(100).make_deposit(10).make_deposit(15).make_withdrawal(25).display_user_balance()

goku.make_deposit(150).make_deposit(10).make_withdrawal(10).make_withdrawal(55).display_user_balance()

vegeta.make_deposit(200).make_withdrawal(10).make_withdrawal(55).display_user_balance()

mike.transfer_money(10,vegeta)

vegeta.display_user_balance()

mike.display_user_balance()