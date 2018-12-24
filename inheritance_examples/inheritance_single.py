class Bank:
    cash=100000
    #@classmethod
    def available_cash(self):
        print("availabe cash",self.cash)

class AndhraBank(Bank):  #two subclasses Andhra and State banks created from single super class Bank
    pass

class StateBank(Bank):
    cash=200000
    #@classmethod
    def available_cash(self):
        print("cash @ bank",Bank.cash)
        print("cash @ StateBank", self.cash)
        print("Total cash",Bank.cash+self.cash)

a=AndhraBank()
a.available_cash()
s=StateBank()
s.available_cash()
