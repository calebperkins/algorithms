def sieve():
    q = 2
    composites = {} # maps nonprimes to a list of primes that made it composite

    while True:
        if q in composites:
            for p in composites[q]:
                composites.setdefault(q + p, []).append(p)
            del composites[q]
        else:
            yield q
            composites[q * q] = [q]
        q += 1


def trial_division():
    primes = [2]
    n = 3
    yield 2
    while True:
        if all(n % p != 0 for p in primes):
            yield n
            primes.append(n)
        n += 2



def prime_factors(n):
    # instead of doing next(primes), repeatedly divide by m, m + 1, etc and decrease n.
    # thats faster because you arent dividing by the same primes over and over
    factors = {}
    m = 2
    while n > 1:
        multiplicity = 0
        while n % m == 0:
            multiplicity += 1
            n /= m
        if multiplicity > 0:
            factors[m] = times
        m += 1
    return factors


print prime_factors(24)
