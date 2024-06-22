import random as re
# import the random data use this 

def main():
    level = get_level()
    score = stimulate_game(level)
    print("Score: ", score)

def get_level():
    while True :
        try :
            level = int(input("Level: "))
            if level in [1,2,3] :
                return level
        except :
            pass
def generate_integer(level):
    if level == 1 :
        x = re.randint(0,9)
        y = re.randint(0,9)
    elif level == 2 :
        x = re.randint(10,99)
        y = re.randint(10,99)
    else :
        x = re.randint(100,999)
        y = re.randint(100,999)
    return x,y
def stimulate_round(x,y) :
    count_tries = 1
    while count_tries <= 3 :
        try :
            answer = int(input(f"{x} + {y} = "))
            if answer == x+y :
                return True
            else :
                count_tries += 1
                print("EEE")
        except :
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False
def stimulate_game(level) :
    count_round = 1
    score = 0
    while count_round <= 10 :
        x, y = generate_integer(level)
        response = stimulate_round(x,y)
        if response == True :
            score += 1
        count_round += 1
    return score

if __name__ == "__main__":
    main()
