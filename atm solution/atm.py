class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
    def withdraw(self, requested_money):
        print "Welcome to " + self.bank_name
        print "Current balance = " + str(self.balance)
        print "Withdraw = " + str(requested_money)
        print "=" * 20
        if requested_money > self.balance:
            print "Can't give you all this money!!!"
        elif requested_money <= 0:
            print "Wrong amount, try again!"
        
        else:
            self.balance = self.balance - requested_money
            avcur = [100,50,10,5,1]
            for i in avcur:
                while requested_money >= i:
                    print "Give " + str(i)
                    requested_money -= i
                if requested_money == 0:
                    break
            print "Remaining balance = " + str(self.balance)
        print "=" * 20
atm1 = ATM(500, "Smart Bank")
atm2 = ATM(1000, "Baraka Bank")
atm3 = ATM(20000, "Tasleef Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)
