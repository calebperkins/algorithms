# https://en.wikipedia.org/wiki/Disjoint-set_data_structure
# Includes union by rank and path compression.

import collections


class DisjointSet(object):

    """A data structure for Union-Find."""

    def __init__(self, elements):
        self.members = {e: DisjointSet.Node() for e in elements}

    def _find(self, e):
        return self.members[e].root()

    def union(self, u, v):
        assert u in self.members
        assert v in self.members

        x = self._find(u)
        y = self._find(v)
        x.union(y)

    def connected_components(self):
        cc = collections.defaultdict(set)
        for u in self.members.keys():
            cc[self._find(u)].add(u)
        return cc.values()

    class Node(object):

        """Internal class for carrying parent information"""

        def __init__(self):
            self.rank = 0
            self.parent = None

        def root(self):
            # recursive with path compression
            if self.parent is not None:
                self.parent = self.parent.root()
            return self if self.parent is None else self.parent

        def union(self, other):
            if self is other:
                return

            if self.rank < other.rank:
                self.parent = other
            elif self.rank > other.rank:
                other.parent = self
            else:
                other.parent = self
                self.rank += 1
