avcur = [100,50,10,5,1]
while True:
    balance = int(raw_input("How much money do you have in your account?\n"))
    if balance > 0:
        break
    else:
        print "Get a job! And try again!"
def withdraw(balance, requestedm):
    if requestedm > balance:
        return balance
    else:
        remainingb = balance - requestedm
    if requestedm <= 0:
        print "Wrong amount, try again!"
    else:
        for i in avcur:
            while requestedm >= i:
                print "Give " + str(i)
                requestedm -= i
            if requestedm == 0:
                break
    return remainingb

while True:
    try:
        requestedm = int(raw_input("How much money do you want?(Enter 'q' to stop)\n"))
    except:
        break
    balance = withdraw(balance, requestedm)
    if not balance:
        continue
    else:
        print "You have $" + str(balance) + " left."
