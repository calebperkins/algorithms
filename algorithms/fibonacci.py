def fibonacci():
    "A lazy stream of Fibonacci numbers."
    a = 0
    b = 1

    while True:
        c = a + b
        a = b
        b = c
        yield c


def index(f):
    "Given a Fibonacci number return its position in the stream."
    i = 0
    for n in fibonacci():
        if f == n:
            return i
        if n > f:
            raise ValueError(str(f) + " is not a fibonacci number")
        i += 1
