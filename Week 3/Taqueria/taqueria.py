menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
tot = 0
while True:
    try:
        data = input("Item: ").title()
        if data in menu:
            tot += menu[data]
            print("Total: $",end="")
            print("{:.2f}".format(tot))
    except EOFError:
        print()
        break

