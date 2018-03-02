avcur = [100,50,10,5,1]
wantedamount = int(raw_input("How much money do you want?\n"))
for i in avcur:
    while wantedamount >= i:
        print "Give " + str(i)
        wantedamount -= i
    if wantedamount == 0:
        break
