from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Iterator


@dataclass(frozen=False)
class Node:
    val: object
    lft: Node | None = None
    rgt: Node | None = None


def preorder(bt: Node) -> Iterator[Node]:
    "A preorder traversal of a binary tree."
    children = [bt]
    while children:
        n = children.pop()
        if n.rgt:
            children.append(n.rgt)
        if n.lft:
            children.append(n.lft)
        yield n.val


def inorder(bst: Node) -> Iterator[Node]:
    "An inorder traversal of a binary tree."
    parents = []

    def traverse_left(n):
        while n is not None:
            parents.append(n)
            n = n.lft

    traverse_left(bst)
    while parents:
        bst = parents.pop()
        yield bst.val
        traverse_left(bst.rgt)


def postorder(root: Node) -> Iterator[Node]:
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

    s = []
    prev = None
    current = root
    while s or current:
        if current:
            s.append(current)
            current = current.lft
        else:
            p = s[-1]
            if p.rgt and prev is not p.rgt:
                current = p.rgt
            else:
                yield p.val
                prev = s.pop()
