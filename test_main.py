from main import add, sub, mul, div

def test_add():
    assert add(3, 1) == {"total":4}
   
def test_sub():
    assert sub(3, 1) == {"total":2}
    
def test_mul():
    assert mul(3, 2) == {"total":6}
    
def test_div():
    assert div(4, 2) == {"total":2}
