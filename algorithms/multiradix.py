import itertools
import operator
import functools


def multiradix_product(M):
    return itertools.product(*(range(x) for x in M))


def product(radixes):
    maximum = functools.reduce(operator.mul, radixes, 1)
    mask = [0] * len(radixes)
    for _ in range(maximum):
        yield tuple(mask)
        _increment(mask, radixes)


def _increment(mask, radixes):
    p = len(mask) - 1
    while p >= 0 and mask[p] == radixes[p] - 1:
        mask[p] = 0
        p -= 1
    mask[p] += 1


def ternary():
    x = [0]
    while True:
        yield tuple(x)
        p = len(x) - 1
        while p >= 0 and x[p] == 2:
            x[p] = 0
            p -= 1
        if p == -1:
            x.insert(0, 1)
        else:
            x[p] += 1


# for x in product([3, 3, 3]):
#     print(x)
