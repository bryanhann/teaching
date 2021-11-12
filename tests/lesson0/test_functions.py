import lp.lesson0.functions as F

def test_inc():
    assert F.inc(0) == 1
    assert F.inc(1) == 2
    assert F.inc(-1) == 0

def test_dec():
    assert F.dec(0) == -1
    assert F.dec(1) ==  0

def test_double():
    assert F.double(0) == 0
    assert F.double(1) == 2
    assert F.double(2) == 4
    assert F.double(-1) == -2
    assert F.double(-2) == -4

def test_square_with_zero():
    assert F.square(0) == 0

def test_square_with_positive_numbers():
    assert F.square(1) == 1
    assert F.square(2) == 4
    assert F.square(3) == 9

def test_square_with_negative_numbers():
    """Squaring negative numbers.

    The results should be positive numbers.
    """
    assert F.square(-1) == 1
    assert F.square(-2) == 4
    assert F.square(-3) == 9

def test_isPositive_with_numbers_around_zero():
    assert F.isPositive(-1) == False
    assert F.isPositive(0) == False
    assert F.isPositive(1) == True

def test_isZero_with_numbers_around_zero():
    assert F.isZero(-1) == False
    assert F.isZero(0) == True
    assert F.isZero(1) == False

