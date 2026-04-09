from algorithms.bloom_filter import BloomFilter


def test_filter():
    f = BloomFilter[str](18, 3)
    assert "hello" not in f
    f.add("hello")
    assert "hello" in f
    f.add("hell")
    assert "hello" in f


def test_repr():
    f = BloomFilter(18, 3)
    assert "BloomFilter(18, 3, 0b0)" == repr(f)
