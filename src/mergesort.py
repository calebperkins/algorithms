# A basic implementation of merge sort - https://en.wikipedia.org/wiki/Merge_sort
# Uses O(log n) stack space and O(n) storage space
# TODO use bottom-up iterative merging instead of recursion, and optimize space usage
# TODO allocate a work array at beginning instead of smaller, more frequent allocations
def mergesort(array):
    return _mergesort(array, 0, len(array) - 1)

def _mergesort(array, left, right):
    if left == right:
        return [array[left]]
    m = (left + right) // 2
    sleft = _mergesort(array, left, m)
    sright = _mergesort(array, m + 1, right)
    return _merge(sleft, sright)

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
    seq = mergesort(seq)
    print("Sorted", seq)
