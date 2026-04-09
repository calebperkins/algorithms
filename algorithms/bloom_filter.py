import random

from collections.abc import Iterable
from typing import TypeVar, Generic

T = TypeVar("T")


class BloomFilter(Generic[T]):
    """
    https://en.wikipedia.org/wiki/Bloom_filter

    m is how many bits in the filter. k is how many hash functions.
    If n is the number of expected elements, the best value for k is m/n ln 2
    """

    def __init__(self, m: int, k: int, array: int = 0):
        self._m: int = m
        self._hashes: int = k
        self._array: int = array

    def _hash(self, elem: T) -> Iterable[int]:
        # use a deterministic RNG
        r = random.Random(elem)
        for _ in range(self._hashes):
            yield r.randint(0, self._m)

    def add(self, elem: T):
        for i in self._hash(elem):
            self._array |= 1 << i

    def __contains__(self, elem: T) -> bool:
        bits = self._hash(elem)
        return all(self._array & (1 << i) for i in bits)

    def __repr__(self) -> str:
        return "BloomFilter(%d, %d, %s)" % (self._m, self._hashes, bin(self._array))
