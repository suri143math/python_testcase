# test_factorial.py

from your_module_name import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive():
    assert factorial(5) == 120

def test_factorial_negative():
    # Factorial is not defined for negative numbers
    try:
        factorial(-2)
    except ValueError as e:
        assert str(e) == "Factorial is not defined for negative numbers."
