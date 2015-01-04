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
    fibs = fibonacci()
    i = 0
    while True:
        n = next(fibs)
        if f == n:
            return i
        if n > f:
            raise ValueError(str(f) + " is not a fibonacci number")
        i += 1

if __name__ == '__main__':
    assert index(13) == 5
