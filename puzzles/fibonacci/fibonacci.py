def fib(n):
    a, b = 0, 1
    if n == 0:
        print(a)
    if n == 1:
        print(b)
    while n > 1:
        a, b = b, a+b
        n -= 1
    return b

print(fib(5))
