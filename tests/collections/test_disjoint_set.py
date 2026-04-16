from algorithms.collections.disjoint_set import DisjointSet


def test_connected_components():
    animals = ["cat", "dog", "bear", "ant", "beatle"]
    ds = DisjointSet[str](animals)
    assert ds.connected_components() == [{a} for a in animals]

    ds.union("cat", "dog")
    ds.union("dog", "bear")
    ds.union("ant", "beatle")

    assert ds.connected_components() == [{"cat", "dog", "bear"}, {"ant", "beatle"}]

    ds.union("bear", "ant")
    assert ds.connected_components() == [{"cat", "dog", "bear", "ant", "beatle"}]
