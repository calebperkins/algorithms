"""
Solution for https://leetcode.com/problems/powx-n/description/
"""


# using O(log n) time, O(log n) space
def mypow_rec(base: int, exp: int) -> int | float:
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp == -1:
        return 1.0 / base
    y = mypow_rec(base, exp // 2)
    y *= y
    if exp % 2 != 0:
        y *= base
    return y


# TODO make this fast by doubling it until we cannot anymore
def _mypow(base, exp) -> int:
    assert exp > 0

    ans = base
    for _ in range(exp - 1):
        ans *= base
    return ans


# without recursion, using O(1) space
def mypow(base: float, exp: int) -> int | float:
    if exp == 0:
        return 1
    answer = _mypow(base, abs(exp))

    if exp < 0:
        return 1 / answer

    return answer
