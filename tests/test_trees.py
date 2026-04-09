import algorithms.trees as t 

def test_tree_traversals():
    f = t.Node("F")
    f.lft = t.Node("B")
    f.rgt = t.Node("G")
    f.lft.lft = t.Node("A")
    f.lft.rgt = t.Node("D")
    f.lft.rgt.lft = t.Node("C")
    f.lft.rgt.rgt = t.Node("E")
    f.rgt.rgt = t.Node("I")
    f.rgt.rgt.lft = t.Node("H")

    assert list(t.preorder(f)) == ["F", "B", "A", "D", "C", "E", "G", "I", "H"]
    assert list(t.inorder(f)) == ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    assert list(t.postorder(f)) == ["A", "C", "E", "D", "B", "H", "I", "G", "F"]
