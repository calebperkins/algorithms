# https://oj.leetcode.com/problems/powx-n/

# using O(log n) time, O(log n) space
# TODO can this be written without recursion, using O(1) space?


def mypow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1.0 / x
    y = mypow(x, n // 2)
    y *= y
    if n % 2 != 0:
        y *= x
    return y
