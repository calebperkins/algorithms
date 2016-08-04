# https://en.wikipedia.org/wiki/Bloom_filter
# m is how many bits in the filter. k is how many hash functions.
# If n is the number of expected elements, the best value for k is m/n ln 2

import random


class BloomFilter:

    def __init__(self, m, k, array=0):
        self._m = m
        self._k = k
        self._array = array

    def _hash(self, key):
        # use a deterministic RNG
        r = random.Random(key)
        for _ in range(self._k):
            yield r.randint(0, self._m)

    def add(self, key):
        for i in self._hash(key):
            self._array |= 1 << i

    def __contains__(self, key):
        bits = self._hash(key)
        return all(self._array & (1 << i) for i in bits)

    def __repr__(self):
        return "BloomFilter(%d, %d, %s)" % (self._m, self._k, bin(self._array))
