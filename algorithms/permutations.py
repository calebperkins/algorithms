def permute(sequence):
    "Given an input sequence, generate all permutations of that sequence."
    if not sequence:
        return
    if len(sequence) == 1:
        yield sequence
        return
    for subseq in permute(sequence[1:]):
        for i in range(len(sequence)):
            copy = list(subseq)
            copy.insert(i, sequence[0])
            yield copy
