from basic_funcs import even_def, avg_def, min_def, max_def

def test_even():
    assert True == even_def(8)
    assert False == even_def(7)

def test_avg():
    a = [1, 3]
    assert isinstance(a, list)
    assert 2 == avg_def(a)

def test_min():
    a = [1, 10, 500]
    assert isinstance(a, list)
    assert 1 == min_def(a)

def test_max():
    a = [1, 10, 500]
    assert isinstance(a, list)
    assert 500 == max_def(a)