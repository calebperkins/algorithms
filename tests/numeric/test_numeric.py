import pytest

from algorithms.numeric import fibonacci
from algorithms.numeric.gray_code import gray_code


def test_fibonacci():
    fib = fibonacci.fibonacci()
    take10 = [next(fib) for i in range(10)]
    assert take10 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci.index(13) == 7


@pytest.mark.parametrize("bits", [0, 1, 2, 3, 4, 8])
def test_gray_code(bits):
    code = gray_code(bits)

    assert len(code) == 2**bits
    assert sorted(code) == list(range(2**bits))
    assert code[0] == 0

    if len(code) > 1:
        for prev, curr in zip(code, code[1:] + code[:1]):
            assert bin(prev ^ curr).count("1") == 1
