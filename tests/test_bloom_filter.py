from algorithms.bloom_filter import *


def test_filter():
    f = BloomFilter(18, 3)
    assert "hello" not in f
    f.add("hello")
    assert "hello" in f
    print(f)
    f.add("hell")
    assert "hell" in f
    print(f)
