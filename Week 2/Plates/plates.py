def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    length = len(s)

    if not s.isalnum():
        return False
    if not s[0:2].isalpha():
        return False
    if not 2 <= length <= 6:
        return False

    i = 0
    while i < length-1:
        if not s[i].isalpha():
            if s[i]=='0':
                return False
            elif not s[i:].isdigit():
                return False
            else:
                return True
        i =i+1

    return True






main()
