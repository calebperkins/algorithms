from algorithms.intervals import Interval, AugmentedTree


def test_tree():
    t = AugmentedTree(Interval(7, 16))
    t.add(Interval(3, 5))
    t.add(Interval(4, 7))
    t.add(Interval(13, 21))
    intersections = list(t.intersecting(Interval(20, 22)))
    assert Interval(13, 21) in intersections
    assert len(intersections) == 1


def test_tree_with_equality():
    t = AugmentedTree(Interval(4, 5))
    assert t.overlaps(Interval(4, 5))
    assert t.overlaps(Interval(5, 7))
    assert t.overlaps(Interval(3, 4))
