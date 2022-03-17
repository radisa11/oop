

class Bank_Account:
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amuoth):
        if(self.balance - amuoth) >= 0:
            self.balance -= amuoth
        else:
            print("you dont have enough money")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        # return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

every_day = Bank_Account(.02,2000)

just_in_case = Bank_Account(.01,100)

every_day.deposit(20).deposit(10).deposit(5).withdraw(10).yeild_interest().display_account_info()
just_in_case.deposit(100).deposit(50).withdraw(50).withdraw(100).withdraw(50).withdraw(49).yeild_interest().display_account_info()

print(every_day.balance)
print(just_in_case.balance)