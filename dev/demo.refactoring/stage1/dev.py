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
