"""
A basic implementation of merge sort - https://en.wikipedia.org/wiki/Merge_sort
Uses O(n) storage space
TODO allocate a work array at beginning instead of smaller, more frequent allocations
and optimize space usage
"""


def mergesort_rec(array: list) -> list:
    "A recursive implementation."

    def _mergesort(lft: int, rgt: int) -> list:
        if lft == rgt:
            return [array[lft]]
        m = (lft + rgt) // 2
        slft = _mergesort(lft, m)
        srgt = _mergesort(m + 1, rgt)
        return _merge(slft, srgt)

    return _mergesort(0, len(array) - 1)


def mergesort(array: list) -> None:
    "A bottom-up, iterative implementation."
    w = 1
    while w <= len(array):
        for i in range(0, len(array), 2 * w):
            a = array[i : i + w]
            b = array[i + w : i + 2 * w]
            merged = _merge(a, b)

            # write sorted, merged array over original array
            for j, v in enumerate(merged, i):
                array[j] = v
        w *= 2


def _merge(xs: list, ys: list) -> list:
    x_i = y_i = 0
    merged = []
    while x_i < len(xs) and y_i < len(ys):
        if xs[x_i] > ys[y_i]:
            merged.append(ys[y_i])
            y_i += 1
        else:
            merged.append(xs[x_i])
            x_i += 1

    # merge remaining list
    rs, r_i = (xs, x_i) if y_i == len(ys) else (ys, y_i)
    while r_i < len(rs):
        merged.append(rs[r_i])
        r_i += 1
    return merged
