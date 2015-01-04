# https://oj.leetcode.com/problems/powx-n/

# using O(log n) time, O(log n) space
# TODO can this be written without recursion, using O(1) space?
def _pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1.0 / x
    y = _pow(x, n // 2)
    y *= y
    if n % 2 != 0:
        y *= x
    return y

if __name__ == '__main__':
    print _pow(34.00515, -3)
    print pow(34.00515, -3)
    print pow(8.88023, 3)
    print _pow(8.88023, 3)
    print pow(8.84372, 10)
    print _pow(8.84372, 10)
