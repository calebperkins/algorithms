from algorithms.rate_limiter import DistributedRateLimiter, RateLimiter


def test_rate_limiter():
    rl = RateLimiter(max_requests=3, window_seconds=10)

    assert rl.allow("alice", 1)  # True  (1 request in [1,10])
    assert rl.allow("alice", 5)  # True  (2 requests in [1,10])
    assert rl.allow("alice", 9)  # True  (3 requests in [1,10])
    assert not rl.allow("alice", 10)  # False (still 3 requests in [1,10])
    assert rl.allow("alice", 12)  # True  (window slides: only 2 requests in [3,12])
    assert rl.allow("bob", 12)  # True  (bob has his own limit)


def test_distributed_rate_limiter():
    rl = DistributedRateLimiter(max_requests=3, window_seconds=10)

    assert rl.allow("alice", 1)  # True  (1 request in [1,10])
    assert rl.allow("alice", 5)  # True  (2 requests in [1,10])
    assert rl.allow("alice", 9)  # True  (3 requests in [1,10])
    assert not rl.allow("alice", 10)  # False (still 3 requests in [1,10])
    assert rl.allow("alice", 12)  # True  (window slides: only 2 requests in [3,12])
    assert rl.allow("bob", 12)  # True  (bob has his own limit)
