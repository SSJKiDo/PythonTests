class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []
        self.withdrawal_time = []


    def withdraw(self, requested_money, available_currency = [100,50,10,5,1]):
        import datetime
        print "Welcome to " + self.bank_name
        print "Current balance = " + str(self.balance)
        print "Withdraw = " + str(requested_money)
        print "=" * 30
        if requested_money > self.balance:
            print "Can't give you all this money!!!"
        elif requested_money <= 0:
            print "Wrong amount, try again!"        
        else:

            self.withdrawals_list.append(requested_money)
            now = datetime.datetime.now()
            self.withdrawal_time.append(str(now.year)+"-"+str(now.month)+"-"+str(now.day)+" "+str(now.hour)+":"+str(now.minute)+":"+str(now.second))
            self.balance -= requested_money
            for i in available_currency:
                while requested_money >= i:
                    print "Give " + str(i)
                    requested_money -= i
                if requested_money == 0:
                    break
            print "Remaining balance = " + str(self.balance)
        print "=" * 30
        return self.balance
    
    def show_withdrawals(self):
        print "Withdrawals: "
        for withdrawaltime, withdrawal in zip(self.withdrawal_time, self.withdrawals_list):
            print str(withdrawal) + " on " + withdrawaltime
        print "=" * 30
        
atm1 = ATM(500, "Smart Bank")
atm2 = ATM(1000, "Baraka Bank")
atm3 = ATM(20000, "Tasleef Bank")
atm1.withdraw(277)
atm1.withdraw(800)
atm1.show_withdrawals()

atm2.withdraw(666)
atm2.withdraw(333)
atm2.show_withdrawals()
