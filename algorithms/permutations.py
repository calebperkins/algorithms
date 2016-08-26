def permute(sequence):
    "Given an input sequence, generate all permutations of that sequence."
    if not sequence:
        return
    if len(sequence) == 1:
        yield sequence
        return
    for subseq in permute(sequence[1:]):
        # for i in range(len(sequence)):
        #     copy = list(subseq)
        #     copy.insert(i, sequence[0])
        #     yield copy
        for ss in next_states(subseq, sequence[0]):
            yield ss


def _permute(sequence):
    perms = [""]
    for i, c in enumerate(sequence):
        x = []
        for perm in perms:
            for state in next_states(perm, c):
                x.append(state)
        perms = x
    return perms


def next_states(sequence, c):
    for i in range(len(sequence)):
        copy = list(sequence)
        copy.insert(i, c)
        yield copy
    yield list(sequence) + [c]
