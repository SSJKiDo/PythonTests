avcur = [100,50,10,5,1]
while True:
    balance = int(raw_input("How much money do you have in your account?\n"))
    if balance > 0:
        break
    else:
        print "Get a job! And try again!"
def withdraw(balance, requested_money):
    if requested_money > balance:
        return balance
    elif requested_money <= 0:
        print "Wrong amount, try again!"
    
    else:
        balance = balance - requested_money
        for i in avcur:
            while requested_money >= i:
                print "Give " + str(i)
                requested_money -= i
            if requested_money == 0:
                break
    return balance

while True:
    try:
        requested_money = int(raw_input("How much money do you want?(Enter 'q' to stop)\n"))
    except:
        break
    balance = withdraw(balance, requested_money)
    if not balance:
        continue
    else:
        print "You have $" + str(balance) + " left."
