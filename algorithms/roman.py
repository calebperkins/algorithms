"""
Convert an integer into a Roman numeral.
"""

import bisect

_numerals = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D",
            1000: "M", 4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}

_breakpoints = sorted(_numerals.keys())

def to_roman(n):
    numerals = []
    while n > 0:
        index = bisect.bisect(_breakpoints, n) - 1
        m = _breakpoints[index]
        numerals.append(_numerals[m])
        n -= m
    return "".join(numerals)
