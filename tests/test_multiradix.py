# from algorithms.multiradix import product
# import itertools
# import unittest
#
#
# class MultiRadixTestCase(unittest.TestCase):
#     def test_decimal_product(self):
#         p = list(product([10]))
#         assert len(p) == 10
#         assert p == [(t,) for t in range(10)]
#
#
#     def test_ternary_product(self):
#         p = product([3, 3, 3])
#         p = list(p)
#         assert len(p) == 27
#         assert p[0] == (0, 0, 0)
#         assert p[13] == (1, 1, 1)
#         assert p[26] == (2, 2, 2)
#
#
#     def test_military_time(self):
#         # sixty seconds per minute, sixty minutes per hour, 24 hours per day
#         p = product([24, 60, 60])
#         for i, combo in enumerate(p):
#             a, b, c = combo
#             print(i, combo)
#             # print("WDDDD")
#             self.assertEqual(i + 1, (a + 1) * (b + 1) * (c + 1))
