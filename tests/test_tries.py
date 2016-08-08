from algorithms.tries import *
import unittest


class TrieTestCase(unittest.TestCase):
    def test_trie(self):
        t = TrieMap()
        self.assertNotIn("hello", t)
        t["hello"] = "world"
        self.assertIn("hello", t)
        self.assertNotIn("hell", t)
        self.assertEqual(t["hello"], "world")
        t["hellos"] = "pork"
        x = list(t.by_prefix("hell"))
        self.assertIn("world", x)
        self.assertIn("pork", x)
