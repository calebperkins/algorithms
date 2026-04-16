from algorithms.cache import LRUCache


def test_small():
    c = LRUCache(1)
    assert len(c) == 0
    c["foo"] = 7
    assert "foo" in c
    assert len(c) == 1
    c["bar"] = 8
    assert "bar" in c
    assert "foo" not in c
    assert len(c) == 1


def test_bigger():
    c = LRUCache(2)
    assert len(c) == 0
    c["foo"] = 1
    c["bar"] = 2
    c["baz"] = 3
    assert "foo" not in c
    assert "bar" in c
    assert "baz" in c
    c["fff"] = 8
    assert "bar" not in c
    assert "baz" in c
    assert "fff" in c
