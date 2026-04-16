import heapq
import typing

T = typing.TypeVar("T")


class PriorityQueue(typing.Generic[T]):
    def __init__(self):
        self._heap: list[tuple[int, T]] = []

    def push(self, item: T, priority: int):
        heapq.heappush(self._heap, (priority, item))

    def pop(self) -> T:
        return heapq.heappop(self._heap)[1]

    def peek(self) -> T | None:
        if self._heap:
            return self._heap[0][1]

    def __bool__(self) -> bool:
        return bool(self._heap)
