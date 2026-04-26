from collections.abc import Collection, Iterator
from typing import TypeVar

T = TypeVar("T")

# Generate the set of all subsets (the power set).

# There are 2^N members in the set. Each integer in that range is a bit mask
# definining which members of the set are to be included.


def power_set(coll: Collection[T]) -> Iterator[list[T]]:
    n = len(coll)
    for mask in range(pow(2, n)):
        yield [elem for i, elem in enumerate(coll) if (mask >> i) & 1]
