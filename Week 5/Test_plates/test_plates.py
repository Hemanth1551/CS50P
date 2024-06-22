from plates import is_valid

def main():
    test_min_max_length()
    test_two_chars_at_begin()
    test_middle_numbers()
    test_zero_is_first_number()
    test_punctuation()

def test_min_max_length():
    assert is_valid("HH") == True
    assert is_valid("Venkat") == True
    assert is_valid("a") == False
    assert is_valid("DommetiHemanth") == False

def test_two_chars_at_begin():
    assert is_valid("he") == True
    assert is_valid("h1") == False
    assert is_valid("1h") == False
    assert is_valid("44") == False

def test_middle_numbers():
    assert is_valid("Hem15") == True
    assert is_valid("hem15r") == False

def test_zero_is_first_number():
    assert is_valid("he1551") == True
    assert is_valid("he0551") == False

def test_punctuation():
    assert is_valid("sai!!") == False


if __name__ == "__main__":
    main()
