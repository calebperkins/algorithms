from algorithms.permutations import permute


def test_permute():
    perms = permute("cats")
    dups = set("".join(x) for x in perms)
    assert len(perms) == 24
    assert len(dups) == 24


def test_permute_ore():
    c0 = permute([])
    assert len(c0) == 0
    c1 = permute(["x"])
    assert len(c1) == 1
    c2 = permute([7, 34])
    assert len(c2) == 2
    c24 = set("".join(perm) for perm in permute(["a", "b", "c", "d"]))
    assert len(c24) == 24
