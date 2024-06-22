def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# they call him by test's

def is_valid(s):
    count=0
    if len(s) < 2 or len(s) > 6 :
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False :
        return False
    i = 0
    x = 0
    while i < len(s) :
        if s[i].isalpha() == False and count == 0 :
            x = i
            if s[i] == "0" :
                return False
            else:
                break
        elif x == 0 :
            i+=1
        else:
            break
    while x < len(s) :
        if i < len(s) :
            if s[i].isalpha() == True :
                return False
            i+=1
        x+=1
    for c in s :
        if c in ["."," ","!","?"] :
            return False
    return True


if __name__ == "__main__":
    main()
