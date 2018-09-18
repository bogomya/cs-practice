# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
import math
def primeNumbers(n):
    sieve = list(map(lambda i: True, range(0,n+1)))
    for divider in range(2, math.floor(math.sqrt(n))+1):
        if(sieve[divider]):
            for i in range(divider*divider, n+1, divider):
                sieve[i] = False
    result = []
    for key, isPrime in enumerate(sieve):
        if(isPrime and key > 1):
            result.append(key)
    return result

if __name__ == '__main__':
    print(primeNumbers(100))
