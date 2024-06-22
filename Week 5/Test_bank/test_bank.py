# import bank
# import both ways to run
from bank import value

def main() :
    test_value_0()
    test_value_20()
    test_value_100()

def test_value_0():
    assert value("hello") == 0
    assert value("heLlO") == 0
def test_value_20():
    assert value("Hey") == 20
    assert value("hEy bRo") == 20
def test_value_100():
    assert value("wHATSaPP") == 100
    assert value("FoOL") == 100

if __name__ == "__main__" :
    main()
