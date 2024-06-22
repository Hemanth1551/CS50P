data = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
data = data.lower()
data = data.replace(" ","")
list = ["42","forty-two","fortytwo"]
if data in list:
    print("yes")
else:
    print("no")
