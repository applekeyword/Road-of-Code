import pytest
from jar import Jar

def test_capacity_greater_than_zero():
    with pytest.raises(ValueError):
        Jar(0)

def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3

def test_deposit_too_many_cookies():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw_not_enough_cookies():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(5)

def test_str():
    jar = Jar()
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
