from algorithms.bloom_filter import *
import unittest


class BloomFilterTestCase(unittest.TestCase):
    def test_filter(self):
        f = BloomFilter(18, 3)
        self.assertNotIn("hello", f)
        f.add("hello")
        self.assertIn("hello", f)
        f.add("hell")
        self.assertIn("hello", f)

    def test_repr(self):
        f = BloomFilter(18, 3)
        self.assertEqual("BloomFilter(18, 3, 0b0)", repr(f))
