import pytest

from algorithms.numeric import fibonacci
from algorithms.numeric.gray_code import gray_code
from algorithms.numeric.pow import mypow


def test_fibonacci():
    fib = fibonacci.fibonacci()
    take10 = [next(fib) for i in range(10)]
    assert take10 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci.index(13) == 7


def test_gray_code():
    for c in gray_code(4):
        print("{0:04b}".format(c))


def test_mypow():
    assert mypow(34.00515, -3) == pytest.approx(pow(34.00515, -3))
    assert mypow(8.88023, 3) == pytest.approx(pow(8.88023, 3))
    assert mypow(8.84372, 10) == pytest.approx(pow(8.84372, 10))
