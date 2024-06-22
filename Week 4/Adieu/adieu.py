import inflect
p = inflect.engine()
a = []
while True :
    try :
        name = input("Name: ")
        a.append(name)
    except (EOFError) :
       print()
       break
result = p.join(a)
print(f"Adieu, adieu, to {result}")
