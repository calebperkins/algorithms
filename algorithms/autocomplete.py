from __future__ import annotations

import string
from collections.abc import Callable, Iterator
from dataclasses import dataclass


@dataclass
class Node:
    value: str | None
    children: dict[str, Node]


def _ascii_children(node: Node) -> Iterator[Node]:
    # instead of sorting the keys, look up each 26 characters in order for O(1)
    for char in reversed(string.ascii_lowercase):
        if char in node.children:
            yield node.children[char]


def _unicode_children(node: Node) -> Iterator[Node]:
    for char, child in sorted(node.children.items(), reverse=True):
        yield child


def _traverse(
    root: Node, extractor: Callable[[Node], Iterator[Node]]
) -> Iterator[Node]:
    stack = [root]
    while stack:
        n = stack.pop()
        yield n
        for child in extractor(n):
            stack.append(child)


class Autocomplete:
    def __init__(self, ascii_only=False) -> None:
        self._root = Node(None, {})
        self._extractor = _ascii_children if ascii_only else _unicode_children

    def insert(self, word: str) -> None:
        """Add a word to the dictionary."""
        node = self._root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(None, {})
            node = node.children[char]
        node.value = word

    def completions(self, prefix: str) -> list[str]:
        """Return all words in the dictionary that start with prefix,
        in alphabetical order."""
        node = self._root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        return [n.value for n in _traverse(node, self._extractor) if n.value]
