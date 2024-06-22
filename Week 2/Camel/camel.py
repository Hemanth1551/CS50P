str = input("camelCase: ")
for i in str:
    if i.isupper():
        str = str.replace(i,"_"+i)
print("snake_case: "+str.lower())
