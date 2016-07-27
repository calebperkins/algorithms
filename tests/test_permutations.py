import unittest
from algorithms.permutations import permute

class PermutationsTestCase(unittest.TestCase):
    def test_permute(self):
        perms = list(permute("cats"))
        dups = set("".join(x) for x in perms)
        self.assertEqual(len(perms), 24)
        self.assertEqual(len(dups), 24)
