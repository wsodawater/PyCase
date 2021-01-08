import pytest
import yaml

def add (a,b):
    return a+b
@pytest.mark.parametrize("a",[1,2,3])
@pytest.mark.parametrize("b",[4,5,6])

def test_add (a,b):
    print("a->%s,b->%s"%(a,b))