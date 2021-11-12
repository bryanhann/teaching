import pytest

def radd( seq ):
    acc = seq[0]
    for item in seq[1:]:
        acc = acc + item
    return acc

def rmul( seq ):
    acc = seq[0]
    #for item in seq[1:]
    for item in seq[1:]:
        acc = acc * item
    return acc

def test_radd():
    assert radd( [1,2,3,4] ) == 10
    assert radd( [0,1,2,3,4] ) == 10
    assert radd( [1] ) == 1
    assert radd( [0] ) == 0

def test_rmul():
    assert rmul( [2,3,4] ) == 24
    assert rmul( [1,2,3,4] ) == 24
    assert rmul( [0,1,2,3,4] ) == 0
    assert rmul( [1] ) == 1
    assert rmul( [0] ) == 0

def test_radd_empty_sequence():
    with pytest.raises( IndexError ):
        x = radd( [] )
def test_rmul_empty_sequence():
    with pytest.raises( IndexError ):
        x = rmul( [] )

