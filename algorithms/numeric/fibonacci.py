from collections.abc import Iterator


def fibonacci() -> Iterator[int]:
    "A lazy stream of Fibonacci numbers starting at 0 (0, 1, 1, 2, 3, 5, ...)."
    a = 0
    b = 1
    while True:
        yield a
        c = a + b
        a = b
        b = c


def index(f: int) -> int | None:
    "Given a Fibonacci number return its position in the stream."
    if f < 0:
        return
    for i, n in enumerate(fibonacci()):
        if f == n:
            return i
        if n > f:
            return
