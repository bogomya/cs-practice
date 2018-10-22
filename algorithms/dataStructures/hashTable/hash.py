from math import sqrt

def isPrime(n):
    d_max = sqrt(n)

    if n == 2:
        return True
    if n % 2 == 0:
        return False

    d = 3
    while n % d != 0 and d <= d_max:
        d += 2

    return d > d_max


def firstPriveGreatherThan(min):
    for n in range(min + 1, min * 2):
        if isPrime(n):
            return n
    return None


def polyhashPrime(word, coefficient, primeNumber, m):
    hash = 0
    for c in word:
        hash = (hash * coefficient + ord(c)) % primeNumber # primeNumber should be more than count of all possible keys

    return abs(hash % m)


def polyhashNoprime(word, coefficient, m):
    hash = 0
    for c in word:
        hash = (hash * coefficient + ord(c))

    return abs(hash % m)


def linearProbingHash(key, coefficient, m, attempt):
    hash = 0
    for c in key:
        hash = (hash * coefficient + ord(c))

    return (hash + attempt) % m
