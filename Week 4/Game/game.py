import random as re
while True :
    try :
        item = int(input("Level: "))
        if item > 0 :
            break
    except :
        pass
rand_num = re.randint(1,item)
while True :
    try :
        guess = int(input("Guess: "))
        if guess > 0 :
            if guess > rand_num :
                print("Too large!")
            elif guess < rand_num :
                print("Too small!")
            else:
                print("Just right!")
                break
    except :
        pass
