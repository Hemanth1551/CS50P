data = input("Fraction:")
while(len(data)!=0):
    try:
        x,y = data.split("/")
        x = int(x)
        y = int(y)
        data = x/y
        data = int(round(data,2)*100)
        if (data == 0) | (data == 1):
            print("E")
            break
        elif (data == 100) | (data == 99):
            print("F")
            break
        elif 100 < data:
            data = input("Fraction:")
        else:
            res = list(str(data))
            res.append("%")
            res = ''.join(res)
            print(res)
            break
    except (ZeroDivisionError,ValueError):
        data = input("Fraction:")
