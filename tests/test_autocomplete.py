from algorithms.autocomplete import Autocomplete


def test_completions():
    ac = Autocomplete()
    ac.insert("bagel")
    ac.insert("bag")
    ac.insert("bat")
    ac.insert("cat")
    assert ac.completions("b") == ["bag", "bagel", "bat"]
    assert ac.completions("ca") == ["cat"]
