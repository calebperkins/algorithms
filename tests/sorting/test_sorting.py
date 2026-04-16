import random

from algorithms.sorting import mergesort as m
from algorithms.sorting import quicksort as q


def test_quicksort():
    seq = [random.randint(-10, 10) for n in range(20)]
    q.quicksort(seq)
    assert sorted(seq) == seq


def test_mergesort():
    seq = [random.randint(-10, 10) for n in range(20)]
    m.mergesort(seq)
    assert sorted(seq) == seq


def test_mergesort_rec():
    seq = [random.randint(-10, 10) for n in range(20)]
    m.mergesort_rec(seq)
    assert sorted(seq) == seq
