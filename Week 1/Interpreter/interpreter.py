exp = input("Expression: ")
x, y, z = exp.split(" ")
x = int(x)
z = int(z)
match y:
    case "+":
        print(float(x+z))
    case "-":
        print(float(x-z))
    case "*":
        print(float(x*z))
    case "/":
        print(float(x/z))
