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
        r = random.Random(key)
        for i in range(self.k):
            yield r.randint(0, self.m)
    def add(self, key):
        for h in self._hash(key):
            self._set_bit(h)
    def __contains__(self, key):
        bits = self._hash(key)
        return all(self._check_bit(bit) for bit in bits)
    def _check_bit(self, i):
        return bool(1 & (self.array >> i))
    def _set_bit(self, i):
        self.array |= 1 << i
    def __repr__(self):
        return bin(self.array)

if __name__ == '__main__':
    f = BloomFilter(18, 3)
    assert "hello" not in f
    f.add("hello")
    assert "hello" in f
    print(f)
    f.add("hell")
    assert "hell" in f
    print(f)
