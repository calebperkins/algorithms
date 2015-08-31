def fibonacci():
    "A lazy stream of Fibonacci numbers starting at 0 (0, 1, 1, 2, 3, 5, ...)."
    a = 0
    b = 1
    while True:
        yield a
        c = a + b
        a = b
        b = c


def index(f):
    "Given a Fibonacci number return its position in the stream."
    if f < 0:
        raise ValueError("%d is not a fibonacci number" % f)
    for i, n in enumerate(fibonacci()):
        if f == n:
            return i
        if n > f:
            raise ValueError("%d is not a fibonacci number" % f)
