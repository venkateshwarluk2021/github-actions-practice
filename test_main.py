from main import add, subtract


def test_add():
    assert add(2, 3)==5
    assert add(1, -1)==0


def test_subtract():
    assert subtract(11, 3)==8
    assert subtract(5, -5)==10
