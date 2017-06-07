class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder(bt):
    "A preorder traversal of a binary tree"
    children = [bt]
    while children:
        n = children.pop()
        if n.right:
            children.append(n.right)
        if n.left:
            children.append(n.left)
        yield n.val


def inorder(bst):
    "An inorder traversal of a binary tree"
    parents = []

    def traverse_left(n):
        while n is not None:
            parents.append(n)
            n = n.left
    traverse_left(bst)
    while parents:
        bst = parents.pop()
        yield bst.val
        traverse_left(bst.right)


def postorder(root):
    # if root.left:
    #     for n in postorder(root.left):
    #         yield n
    # if root.right:
    #     for n in postorder(root.right):
    #         yield n
    # yield root.val

    # prev = None
    # s = [root]
    # while s:
    #     c = s[-1]
    # going down
    #     if not prev or prev.left is c or prev.right is c:
    #         if c.left:
    #             s.append(c.left)
    #         elif c.right:
    #             s.append(c.right)
    #         else:
    #             yield c.val
    #             s.pop()
    # traversing up from left
    #     elif c.left is prev:
    #         if c.right:
    #             s.append(c.right)
    #         else:
    #             yield c.val
    #             s.pop()
    # traversing up from right
    #     elif c.right is prev:
    #         yield c.val
    #         s.pop()
    #     prev = c

    s = []
    prev = None
    current = root
    while s or current:
        if current:
            s.append(current)
            current = current.left
        else:
            p = s[-1]
            if p.right and prev is not p.right:
                current = p.right
            else:
                yield p.val
                prev = s.pop()


if __name__ == '__main__':
    # http://en.wikipedia.org/wiki/Tree_traversal
    f = TreeNode("F")
    f.left = TreeNode("B")
    f.right = TreeNode("G")
    f.left.left = TreeNode("A")
    f.left.right = TreeNode("D")
    f.left.right.left = TreeNode("C")
    f.left.right.right = TreeNode("E")
    f.right.right = TreeNode("I")
    f.right.right.left = TreeNode("H")

    assert list(preorder(f)) == ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    assert list(inorder(f)) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    assert list(postorder(f)) == ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']
