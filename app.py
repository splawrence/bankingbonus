import savingsaccount

def main():
    account = getInfo()
    selection = ""

    print ("D = Deposit, W = Withdrawal, Q = Quit")
    while selection.upper() != "Q":
        selection = input("Enter D, W, or Q: ")
        if selection.upper() == "D":
            account.makeDeposit(int(input("Enter amount to deposit:")))
        elif selection.upper() == "W":
            account.makeWithdrawal(int(input("Enter amount to withdraw:")))
    print ("End of Transactions. Have a good day", account._name.title(),".")

def getInfo():
    name = input ("Enter person's name: ")
    savingsAcct = savingsaccount.SavingsAccount(name, 0)
    return savingsAcct

main()

class SavingsAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def makeDeposit(self, deposit):
       self._balance += deposit
       print ("Balance: " ,"${:,.2f}".format(self._balance))

    def makeWithdrawal(self, withdrawal):
        if (self._balance >= withdrawal):
            self._balance -= withdrawal
            print ("Balance: " ,"${:,.2f}".format(self._balance))
        else:
            print ("Insufficient funds, transaction denied!")

