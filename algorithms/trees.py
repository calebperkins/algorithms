from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(frozen=False)
class Node:
    val: object
    lft: Node | None = None
    rgt: Node | None = None


def preorder(node: Node) -> Iterator[Node]:
    "A preorder traversal of a binary tree."
    children = [node]
    while children:
        n = children.pop()
        if n.rgt:
            children.append(n.rgt)
        if n.lft:
            children.append(n.lft)
        yield n


def inorder(node: Node) -> Iterator[Node]:
    "An inorder traversal of a binary tree."
    parents: list[Node] = []

    def traverse_left(n: Node | None):
        while n is not None:
            parents.append(n)
            n = n.lft

    traverse_left(node)
    while parents:
        n = parents.pop()
        yield n
        traverse_left(n.rgt)


def postorder(node: Node) -> Iterator[Node]:
    "A postorder traversal of a binary tree."
    # if root.lft:
    #     for n in postorder(root.lft):
    #         yield n
    # if root.rgt:
    #     for n in postorder(root.rgt):
    #         yield n
    # yield root.val

    # prev = None
    # s = [root]
    # while s:
    #     c = s[-1]
    # going down
    #     if not prev or prev.lft is c or prev.rgt is c:
    #         if c.lft:
    #             s.append(c.lft)
    #         elif c.rgt:
    #             s.append(c.rgt)
    #         else:
    #             yield c.val
    #             s.pop()
    # traversing up from left
    #     elif c.lft is prev:
    #         if c.rgt:
    #             s.append(c.rgt)
    #         else:
    #             yield c.val
    #             s.pop()
    # traversing up from right
    #     elif c.rgt is prev:
    #         yield c.val
    #         s.pop()
    #     prev = c

    stack: list[Node] = []
    prev: Node | None = None
    current: Node | None = node
    while stack or current:
        if current:
            stack.append(current)
            current = current.lft
        else:
            p = stack[-1]
            if p.rgt and prev is not p.rgt:
                current = p.rgt
            else:
                yield p
                prev = stack.pop()
