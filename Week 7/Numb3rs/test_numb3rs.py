from numb3rs import validate

def test_dark():
    assert validate("255.255.255.255")
    assert validate("192.168.1.1")
    assert validate("192.168.1.255")
    assert validate("0.0.0.0")
    assert not validate("192.168.1")
    assert not validate("192.168.1.256")
    assert not validate("192.168.1.255.1")
    assert not validate("512.512.512.512")
    assert not validate("512.512.512.512.512")
    assert not validate("cat")
# we can test the all condition at this
