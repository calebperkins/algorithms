import heapq
import typing

T = typing.TypeVar("T")


class PriorityQueue(typing.Generic[T]):
    def __init__(self):
        self._heap: list[T] = []

    def push(self, item: T):
        heapq.heappush(self._heap, item)

    def pop(self) -> T:
        return heapq.heappop(self._heap)

    def peek(self) -> T | None:
        if self._heap:
            return self._heap[0]

    def __bool__(self) -> bool:
        return bool(self._heap)
