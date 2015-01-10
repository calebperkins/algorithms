"""
Convert an integer into a Roman numeral.
"""

numerals = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}

# Recursive version
def to_roman_rec(n):
    if n == 0:
        return ""
    l = max(m for m in numerals.keys() if m <= n)

    return numerals[l] + to_roman_rec(n - l)

# Iterative version
def to_roman(n):
    acc = []
    while n > 0:
        l = max(m for m in numerals.keys() if m <= n)
        acc.append(numerals[l])
        n -= l
    return "".join(acc)

if __name__ == '__main__':
    assert "I" == to_roman(1)
    assert "VIII" == to_roman(8)
    assert "IV" == to_roman(4)
    assert "VII" == to_roman(7)
    assert "XV" == to_roman(15)
    assert "MMXIV" == to_roman(2014)
    assert "MCMLIV" == to_roman(1954)
