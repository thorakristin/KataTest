from kata import Add

def test_empty_string():
    assert Add("") == 0

def test_single_digit():
    assert Add("1") == 1
