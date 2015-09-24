import collections

Interval = collections.namedtuple("Interval", "start, end")


class AugmentedTree:
    """
    An augmented tree for querying intervals. The nodes are ordered by the start interval. The high attribute is the
    maximum end interval of the node and any of its children.

    This tree could become imbalanced. More advanced augmented trees should be a based on a self-balancing BST.
    """

    def __init__(self, interval):
        self.interval = interval
        self.high = interval.end
        self.left = None
        self.right = None

    def overlaps(self, interval):
        i = self.interval
        return i.end >= interval.start and i.start <= interval.end

    def intersecting(self, interval):
        s = [self]
        while s:
            n = s.pop()
            if n.high < interval.start:
                continue
            if n.overlaps(interval):
                yield n.interval
            if n.right and n.right.interval.start <= interval.end:
                s.append(n.right)
            if n.left:
                s.append(n.left)

    def __lt__(self, other):
        return self.interval.start < other.interval.start

    def add(self, interval):
        # Create a new node and add it to a leaf
        m = AugmentedTree(interval)
        n = self
        while True:
            n.high = max(n.high, m.high)
            if m < n:
                if n.left:
                    n = n.left
                else:
                    n.left = m
                    return
            else:
                if n.right:
                    n = n.right
                else:
                    n.right = m
                    return
