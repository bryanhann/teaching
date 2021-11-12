import pytest
from dev import radd, rmul

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

