# Given an input sequence, generate all permutations of that sequence.
def permute(sequence):
    if len(sequence) <= 1:
        for n in sequence:
            yield [n]
    for i in range(len(sequence)):
        sequence[0], sequence[i] = sequence[i], sequence[0]
        for subseq in permute(sequence[1:]):
            yield [sequence[0]] + subseq

if __name__ == '__main__':
    # Test cases
    c1 = list(permute([1,2,3,4]))
    assert len(c1) == 24
