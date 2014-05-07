from pushgp.push.interpreter import Push
from pushgp.push.instructions import float


def test_add():
    assert Push()(float.add, 1.0, 1.0)['float'] == [2.0]


def test_sub():
    assert Push()(float.sub, 2.0, 1.0)['float'] == [1.0]


def test_mult():
    assert Push()(float.mult, 2.0, 1.0)['float'] == [2.0]


def test_div():
    assert Push()(float.div, 2.0, 1.0)['float'] == [2.0]
    assert Push()(float.div, 2.0, 0.0)['float'] == []
