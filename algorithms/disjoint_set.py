from __future__ import annotations
import collections
from typing import TypeVar, Generic

T = TypeVar("T")


# https://en.wikipedia.org/wiki/Disjoint-set_data_structure
# Includes union by rank and path compression.
class DisjointSet(Generic[T]):
    """A data structure for Union-Find."""

    def __init__(self, elements: list[T]):
        self.members: dict[T, DisjointSet.Node] = {
            e: DisjointSet.Node() for e in elements
        }

    def _find(self, e):
        return self.members[e].root()

    def union(self, u: T, v: T):
        assert u in self.members
        assert v in self.members

        x = self._find(u)
        y = self._find(v)
        x.union(y)

    def connected_components(self) -> list[set[T]]:
        cc = collections.defaultdict(set)
        for u in self.members.keys():
            cc[self._find(u)].add(u)
        return list(cc.values())

    class Node(object):
        """Internal class for carrying parent information"""

        def __init__(self):
            self.rank: int = 0
            self.parent: DisjointSet.Node | None = None

        def root(self) -> DisjointSet.Node:
            # recursive with path compression
            if self.parent is not None:
                self.parent = self.parent.root()
            return self if self.parent is None else self.parent

        def union(self, other: DisjointSet.Node):
            if self is other:
                return

            if self.rank < other.rank:
                self.parent = other
            elif self.rank > other.rank:
                other.parent = self
            else:
                other.parent = self
                self.rank += 1
