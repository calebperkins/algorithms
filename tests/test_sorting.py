from algorithms import quicksort as q
from algorithms import mergesort as m
import random


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
