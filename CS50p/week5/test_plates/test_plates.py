from plates import is_valid


def test_start():
    assert is_valid("H1") == False


def test_len():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("CS50") == True


def test_number():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("AAA222") == True


def test_mark():
    assert is_valid("PI3.14") == False
    assert is_valid("PI!312") == False
    assert is_valid("AA?222") == False
