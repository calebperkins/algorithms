from algorithms import quicksort as q
import random


def test_sorting():
    seq = [random.randint(-10, 10) for n in range(20)]
    q.quicksort(seq)
    assert sorted(seq) == seq
