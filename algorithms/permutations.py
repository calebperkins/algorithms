# Given an input sequence, generate all permutations of that sequence.
def permute(sequence):
    if len(sequence) == 1:
        yield sequence
    for i in range(len(sequence)):
        sequence[0], sequence[i] = sequence[i], sequence[0]
        for subseq in permute(sequence[1:]):
            yield [sequence[0]] + subseq