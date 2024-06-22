def main():
    data = input("Fraction: ")
    percentage = convert(data)
    result = gauge(percentage)
    print(result)

def convert(fraction):
    while True:
        try :
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            z = x / y
            if z<= 1:
                p = int(z*100)
                return p
            else:
                fraction = input("fraction: ")
        except (ValueError, ZeroDivisionError) :
            raise

def gauge(percentage):
    p = percentage
    if p >= 99 :
        return "F"
    elif p <= 1 :
        return "E"
    else :
        return (f"{round(p)}%")


if __name__ == "__main__":
    main()
