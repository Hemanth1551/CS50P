def main():
    mes = input("Input: ")
    mes_w_v = shorten(mes)
    print("Output: "+mes_w_v)

def shorten(word):
    for i in word :
        if i.upper() in ["A","E","I","O","U"] :
            word = word.replace(i,"")
    return word

if __name__ == "__main__":
    main()


# it will test by test case's
