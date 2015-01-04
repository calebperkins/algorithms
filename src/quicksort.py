# An in-place quicksort.
# http://en.wikipedia.org/wiki/Quicksort

import random

def quicksort(array):
    _quicksort(array, 0, len(array) - 1)

def _quicksort(array, left, right):
    if left >= right:
        return

    s_i = _partition(array, left, right)
    _quicksort(array, left, s_i - 1)
    _quicksort(array, s_i + 1, right)

def _partition(array, left, right):
    p_i = _choose_pivot(array, left, right)
    p = array[p_i]
    array[p_i], array[right] = array[right], array[p_i]

    s_i = left
    for i in range(left, right): # does not include right
        v = array[i]
        if v < p:
            array[i], array[s_i] = array[s_i], array[i]
            s_i += 1

    array[s_i], array[right] = array[right], array[s_i]
    return s_i

def _choose_pivot(array, left, right):
    # Use the middle as the pivot. You could also use a strategy based on
    # randomization, averaging, etc
    return (left + right) // 2

if __name__ == '__main__':
    seq = [random.randint(-10, 10) for n in range(20)]
    print("Unsorted", seq)
    quicksort(seq)
    print("Sorted", seq)
