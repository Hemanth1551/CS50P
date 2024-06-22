Ad = 50
print("Amount Due:",Ad)
while (Ad>0):
    Ic = int(input("Insert Coin: "))
    if Ic == 5 or Ic == 10 or Ic == 25 :
        Ad = Ad - Ic
        if Ad != 0:
            print("Amount Due:",Ad)
    else:
        print("Amount Due:",Ad)
else:
    Ad = str(Ad)
    Ad = Ad.replace("-","")
    print("Change Owed:",Ad)
