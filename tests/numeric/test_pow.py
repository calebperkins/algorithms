from pytest import approx

from algorithms.numeric.pow import mypow


def test_mypow_basic_base():
    assert mypow(9, 0) == 1
    assert mypow(9, 1) == 9


def test_mypow_positive_base_positive_exp():
    assert mypow(8, 3) == 512


def test_mypow_positive_base_negative_exp():
    assert mypow(8, -3) == 1 / 512


def test_mypow_fractional_base():
    assert mypow(8.88023, 3) == approx(pow(8.88023, 3))
    assert mypow(-12.5, 4) == approx(pow(-12.5, 4))


def test_mypow_slow():
    assert mypow(0.00001, 2147483647) == 32
