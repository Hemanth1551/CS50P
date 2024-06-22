import re


def main():
    print(count(input("Text: ")))


def count(s):
    # back word and front word to leave
    regex = "(^|\W)um($|\W)"
    match = re.findall(regex, s, re.IGNORECASE)
    if match:
        return(len(match))


if __name__ == "__main__":
    main()
