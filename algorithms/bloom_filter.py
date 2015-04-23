# https://en.wikipedia.org/wiki/Bloom_filter
# m is how many bits in the filter. k is how many hash functions.
# If n is the number of expected elements, the best value for k is m/n ln 2

import random


class BloomFilter(object):

    def __init__(self, m, k):
        self.array = 0
        self.k = k
        self.m = m

    def _hash(self, key):
        # use a deterministic RNG
        r = random.Random(key)
        for _ in range(self.k):
            yield r.randint(0, self.m)

    def add(self, key):
        for i in self._hash(key):
            self.array |= 1 << i

    def __contains__(self, key):
        bits = self._hash(key)
        return all(1 & (self.array >> i) for i in bits)

    def __repr__(self):
        return bin(self.array)
