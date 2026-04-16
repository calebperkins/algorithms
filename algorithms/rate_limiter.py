from collections import defaultdict, deque

from sortedcontainers import SortedList


class RateLimiter:
    "Allow a max of N requests per T seconds."

    def __init__(self, max_requests: int, window_seconds: int) -> None:
        self._max_requests = max_requests
        self._window_seconds = window_seconds
        self._user_requests: dict[str, deque[int]] = defaultdict(deque)

    def allow(self, user_id: str, timestamp: int) -> bool:
        # the _accepted_ requests
        accepted_requests = self._user_requests[user_id]

        cutoff = timestamp - self._window_seconds

        while accepted_requests and accepted_requests[0] < cutoff:
            accepted_requests.popleft()

        assert len(accepted_requests) <= self._max_requests
        if len(accepted_requests) == self._max_requests:
            return False

        accepted_requests.append(timestamp)
        return True


class DistributedRateLimiter:
    def __init__(self, max_requests: int, window_seconds: int) -> None:
        self._max_requests = max_requests
        self._window_seconds = window_seconds
        self._user_requests: dict[str, SortedList] = defaultdict(SortedList)

    def allow(self, user_id: str, timestamp: int) -> bool:
        # the _accepted_ requests
        accepted_requests = self._user_requests[user_id]

        expired = accepted_requests.bisect_left(timestamp - self._window_seconds)
        del accepted_requests[:expired]

        assert len(accepted_requests) <= self._max_requests
        if len(accepted_requests) == self._max_requests:
            return False

        accepted_requests.add(timestamp)
        return True
