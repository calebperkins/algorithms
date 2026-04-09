from algorithms.permutations import permute


def test_permute():
    perms = list(permute("cats"))
    dups = set("".join(x) for x in perms)
    assert len(perms) == 24
    assert len(dups) == 24
