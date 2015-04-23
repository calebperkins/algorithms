from algorithms.tries import *


def test_trie():
    t = TrieMap()
    assert "hello" not in t
    t["hello"] = "world"
    assert "hello" in t
    assert "hell" not in t
    assert t["hello"] == "world"
    t["hellos"] = "pork"
    x = list(t.by_prefix("hell"))
    assert "world" in x
    assert "pork" in x
