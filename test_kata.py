from kata import Add
import pytest

def test_empty_string():
    assert Add("") == 0

def test_single_digit():
    assert Add("1") == 1

def test_two_digits():
    assert Add("1,2") == 3

def test_unknown_number():
    assert Add("1,2,3,4,5") == 15
    assert Add("10,2,5,22,1,1") == 41

def test_handle_newline():
    assert Add("1\n2,3") == 6

def test_ignore_over_1000():
    assert Add("1001,2") == 2

def test_error_if_negative():
    with pytest.raises(ValueError, match=r"Negatives not allowed:-1"):
        Add("-1,2")

    with pytest.raises(ValueError, match=r"Negatives not allowed:-4,-5"):
        Add("2,-4,3,-5")

def test_support_delimeters():
    Add("//X\n1X2") == 3
    Add("//%\n1%2%3") == 6