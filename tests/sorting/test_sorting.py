import random

import pytest

from algorithms.sorting import mergesort as m
from algorithms.sorting import quicksort as q


@pytest.fixture(autouse=True)
def set_random_seed():
    random.seed(42)


def test_quicksort():
    seq = [random.randint(-10, 10) for n in range(20)]
    q.quicksort(seq)
    assert sorted(seq) == seq


def test_mergesort():
    seq = [random.randint(-10, 10) for n in range(20)]
    m.mergesort(seq)
    assert sorted(seq) == seq


def test_mergesort_rec_tiny():
    seq = [8, 6]
    assert m.mergesort_rec(seq) == [6, 8]


def test_mergesort_rec():
    seq = [random.randint(-10, 10) for n in range(20)]
    assert m.mergesort_rec(seq) == sorted(seq)
