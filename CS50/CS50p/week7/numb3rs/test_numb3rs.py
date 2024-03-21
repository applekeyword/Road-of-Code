from numb3rs import validate

def test_str():
    assert validate("cat") == False
    assert validate("cat.vat.cat.vat") == False


def test_num():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.1000") == False
    assert validate("275.3.6.28") == False
    assert validate("192.168.1.256") == False
    assert validate("192.168.1.255.1") == False
    assert validate("512.512.512.512") == False
    assert validate("512.512.512.512.512") == False


