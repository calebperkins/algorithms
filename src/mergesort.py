# A basic implementation of merge sort - https://en.wikipedia.org/wiki/Merge_sort
# Uses O(n) storage space
# TODO allocate a work array at beginning instead of smaller, more frequent allocations
# and optimize space usage

# A recursive implementation
def mergesort_rec(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    if left == right:
        return [array[left]]
    m = (left + right) // 2
    sleft = mergesort_rec(array, left, m)
    sright = mergesort_rec(array, m + 1, right)
    return _merge(sleft, sright)

# A bottom-up, iterative implementation
def mergesort(array):
    w = 1
    while w <= len(array):
        for i in range(0, len(array), 2 * w):
            a = array[i : i + w]
            b = array[i + w : i + 2 * w]
            merged = _merge(a, b)

            # write sorted, merged array over original array
            for j, v in enumerate(merged):
                array[i + j] = v
        w *= 2

def _merge(sleft, sright):
    i = j = 0
    a = []
    while i < len(sleft) and j < len(sright):
        if sleft[i] > sright[j]:
            a.append(sright[j])
            j += 1
        else:
            a.append(sleft[i])
            i += 1

    # merge remaining list
    r, k = (sleft, i) if j == len(sright) else (sright, j)
    while k < len(r):
        a.append(r[k])
        k += 1
    return a


if __name__ == '__main__':
    import random
    seq = [random.randint(-10,10) for n in range(20)]
    print("Unsorted", seq)
    mergesort(seq)
    print("Sorted", seq)
