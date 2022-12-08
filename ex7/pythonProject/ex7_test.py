from ex7 import *
import ex7_helper


def test_mult():
    assert mult(0, 1) == 0
    assert mult(0.5, 1) == 0.5
    assert mult(5, 5) == 25
    assert mult(2, 4) == 8
    assert mult(4, 2) == 8

def test_is_even():
    assert is_even(5) == False
    assert is_even(1) == False
    assert is_even(2) == True
    assert is_even(0) == True

def test_log_mult():
    assert log_mult(0, 1) == 0
    assert log_mult(0.5, 1) == 0.5
    assert log_mult(5, 5) == 25
    assert log_mult(2, 4) == 8
    assert log_mult(4, 2) == 8
def test_reverse():
    assert reverse('kayak') == 'kayak'
    assert reverse('adc') == 'cda'
    assert reverse('a') == 'a'
    assert reverse('kAyak') == 'kayAk'

def test_is_power():
    assert is_power(2,8) == True
    assert is_power(2, 4) == True
    assert is_power(2, 6) == False
    assert is_power(5, 10) == False
    assert is_power(10, 1) == True
    assert is_power(2, 0) == False
    assert is_power(0,2) == False
    assert is_power(1, 8) == False
    assert is_power(0, 1) == True
