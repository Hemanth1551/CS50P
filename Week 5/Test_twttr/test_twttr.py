# import twttr
from twttr import shorten
def main() :
    test_shorten()
    test_number()
def test_shorten() :
    assert shorten("Hemanth") == "Hmnth"
    assert shorten("SAI") == "S"
    assert shorten("HEma") == "Hm"
def test_number() :
    assert shorten("1234") == "1234"
def test_punctuation() :
    assert shorten("!&") == "!&"
if __name__ == "__main__" :
    main()
def main():
    data=input("Enter String: ")
    x = shorten(data)
    print(x)
