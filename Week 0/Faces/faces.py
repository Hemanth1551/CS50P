def convert(str):
    s = str
    data = str.split()
    for i in data:
        if i==":)":
            s = s.replace(":)","🙂")
        if i==":(":
            s = s.replace(":(","🙁")
    return s
print(convert(input("")))
