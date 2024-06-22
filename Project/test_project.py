from project import stu_on_uni,clg_on_uni,brch_on_uni
import pytest

#def main():
#    test_stu_on_uni()
    #clg_on_uni()
    #brch_on_uni()


def test_stu_on_uni():
    result = stu_on_uni("20L1101101")
    assert result == ["20L1101101", "hemanth", 2020, "clg1", "CSE", 101]

def test_clg_on_uni():
    result = clg_on_uni("L1")
    assert result == ([101, 201], ['hemanth', 'sai'])

    result = clg_on_uni("L2")
    assert result == ([102], ['sai'])

    result = clg_on_uni("L5")
    assert result == "College Was Not Associated With University"

def test_brch_on_uni():
    result = brch_on_uni(101)
    print("Test result 101:", result)
    assert result == ([101, 201], ['L1', 'L1'])

    result = brch_on_uni(102)
    print("Test result 102:", result)
    assert result == ([102], ['L2'])

    result = brch_on_uni(103)
    print("Test result 103:", result)
    assert result == ([103], ['L3'])

    result = brch_on_uni(104)
    print("Test result 104:", result)
    assert result == ([104], ['L4'])

    result = brch_on_uni(105)
    print("Test result 105:", result)
    assert result == (1, 0)

#if __name__ == "__main__":
#    main()
