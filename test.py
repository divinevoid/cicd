from mat import add, sub


def test_add():
    assert add(2, 3) == 5
    assert add(2, -3) == -1
    assert add(4, 6) == 10
    assert add(3, -9) == -6


def test_sub():
    assert sub(2, 3) == -1
    assert sub(3, 3) == 0
    assert sub(5, 2) == 3
    assert sub(2, -2) == 4
