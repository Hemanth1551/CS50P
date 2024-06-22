def main():
    input=input("Enter input: ")
    result = value(input)
    print(f"${result}")
def value(input):
    if input.lower().strip() == "hello":
        return 0
    elif input[0].lower().strip() == "h":
        if input[0:5].lower().strip() == "hello":
            return 0
        else:
            return 20
    else:
        return 100
if __name__ == "__main__":
    main()
