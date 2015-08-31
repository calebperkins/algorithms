from algorithms.power_set import power_set
from algorithms.permutations import permute
from algorithms.disjoint_set import DisjointSet
from algorithms import fibonacci
from algorithms.gray_code import gray_code


def test_power_set():
    s = [1, 2, 3]
    ps = list(power_set(s))
    assert len(ps) == 8


def test_permute():
    c0 = list(permute([]))
    assert len(c0) == 0
    c1 = list(permute(["x"]))
    assert len(c1) == 1
    c2 = list(permute([7, 34]))
    assert len(c2) == 2
    c24 = set("".join(perm) for perm in permute(["a", "b", "c", "d"]))
    assert len(c24) == 24


def test_disjoint_set():
    s = [1, 2, 3, 4, 5]
    ds = DisjointSet(s)
    assert len(ds.connected_components()) == 5
    ds.union(1, 2)
    ds.union(1, 3)
    assert len(ds.connected_components()) == 3


def test_fibonacci():
    fib = fibonacci.fibonacci()
    take10 = [next(fib) for i in range(10)]
    assert take10 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci.index(13) == 7


def test_gray_code():
    code = gray_code(4)
    for c in gray_code(4):
        print("{0:04b}".format(c))
