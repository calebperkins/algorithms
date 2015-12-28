"""
Generate a gray code

https://en.wikipedia.org/wiki/Gray_code
https://oj.leetcode.com/problems/gray-code/
"""

def gray_code(bits):
    "Produce a gray code with the specified number of bits."
    m = 0
    code = [0]
    while m < bits:
        # reverse last sequence and prepend with bit 1
        for x in reversed(code):
            y = x | (1 << m)
            code.append(y)
        m += 1
    return code
