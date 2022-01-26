from main import add
from main import sub
from main import mul
from main import div

def test_add():
    assert {"total":4} == add(3, 1)
   
def test_sub():
    assert {"total":2} == sub(3, 1)
    
def test_mul():
    assert mul(3, 2) == {"total":6}
    
def test_div():
    assert div(4, 2) == {"total":2}
