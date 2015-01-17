"""
Generate a gray code

https://en.wikipedia.org/wiki/Gray_code
https://oj.leetcode.com/problems/gray-code/
"""

# Recursive version
def _gray_code(n):
    if n == 0:
        return [0]
    last = _gray_code(n - 1)
    l = len(last)
    for i in range(l - 1, -1, -1):
        x = last[i]
        y = x | (1 << (n - 1))
        last.append(y)
    return last

# Iterative version
def gray_code(n):
    m = 0
    code = [0]
    length = 1
    while m < n:
        # reverse last sequence and prepend with bit 1
        for i in range(length - 1, -1, -1):
            x = code[i]
            y = x | (1 << m)
            code.append(y)
        m += 1
        length *= 2
    return code

if __name__ == '__main__':
    code = gray_code(4)
    for c in gray_code(4):
        print("{0:04b}".format(c))
