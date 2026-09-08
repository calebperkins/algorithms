from algorithms.graphs import shortest_path as s


def test_simple():
    assert s.shortest_path(
        5,
        [(0, 1, 10), (0, 2, 3), (1, 3, 2), (2, 1, 4), (2, 3, 8), (2, 4, 2), (3, 4, 5)],
        0,
    ) == {0: 0, 1: 7, 2: 3, 3: 9, 4: 5}
