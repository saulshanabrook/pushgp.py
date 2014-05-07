from pushgp.push.interpreter import Push
from pushgp.push.instructions import str


def test_concat():
    assert Push()(str.concat, 'a', 'b')['str'] == ['ab']


def test_length():
    assert Push()(str.length, 's')['int'] == [1]


def test_to_int():
    assert Push()(str.to_int, 's')['int'] == []
    assert Push()(str.to_int, '1')['int'] == [1]
    assert Push()(str.to_int, '1.0')['int'] == []
    assert Push()(str.to_int, '1.0')['float'] == []


def test_reverse():
    assert Push()(str.reverse, 'ab')['str'] == ['ba']


def test_to_chars():
    assert Push()(str.to_chars, 'ab')['str'] == ['b', 'a']
    assert Push()(str.to_chars, 's')['str'] == ['s']


def test_contained():
    assert Push()(str.contained, 's', 'ss')['bool'] == [True]
    assert Push()(str.contained, 'ss', 's')['bool'] == [False]
