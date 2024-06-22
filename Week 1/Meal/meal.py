def main():
    time = input("What time is it? ")
    k = convert(time)
    if (0<=k) & (k<=8):
        print("breakfast time")
    elif (8<=k) & (k<=13):
        print("lunch time")
    elif (14<=k) & (k<=24):
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    minutes = (minutes/6)/10
    i = float(hours+minutes)
    return i

if __name__ == "__main__":
    main()
