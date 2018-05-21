# simulation of veery basic bank account

class BankAccount:
    def __init__(self, moneey):
        self.money = float(moneey)

    def addMoney(self, money):
        self.money += money

    def ATMSimulator(self, amount):
        if self.money < amount:
            print 'Your bank balance is too low'
        else:
            self.money -= amount

    def balance(self):
        return self.money


myAccount = BankAccount(300)
myAccount.addMoney(100)
myAccount.ATMSimulator(200)
print 'Bank account balance is: %f ' % myAccount.balance()
