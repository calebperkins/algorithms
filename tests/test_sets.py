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
    c1 = list(permute([1, 2, 3, 4]))
    assert len(c1) == 24
    c2 = list(permute([]))
    assert len(c2) == 0


def test_disjoint_set():
    s = [1, 2, 3, 4, 5]
    ds = DisjointSet(s)
    assert len(ds.connected_components()) == 5
    ds.union(1, 2)
    ds.union(1, 3)
    assert len(ds.connected_components()) == 3


def test_fibonacci():
    assert fibonacci.index(13) == 5


def test_gray_code():
    code = gray_code(4)
    for c in gray_code(4):
        print("{0:04b}".format(c))
