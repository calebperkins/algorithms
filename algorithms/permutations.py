def permute(sequence):
    "Given an input sequence, generate all permutations of that sequence."
    if not sequence:
        return []
    perms = [tuple()]
    for elem in sequence:
        next_perms = []
        for perm in perms:
            for next_perm in _add_element(perm, elem):
                next_perms.append(next_perm)
        perms = next_perms
    return perms


def _add_element(sequence, elem):
    for i in range(len(sequence) + 1): # insert elem in every position
        copy = list(sequence)
        copy.insert(i, elem)
        yield copy
