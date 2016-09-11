import heapq


class PriorityQueue:
    def __init__(self):
        self._heap = []

    def push(self, item):
        heapq.heappush(self._heap, item)

    def pop(self):
        return heapq.heappop(self._heap)

    def peek(self):
        return self._heap[0]
