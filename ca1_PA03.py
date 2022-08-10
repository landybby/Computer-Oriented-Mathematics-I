import math


def sieve(n):
    if n < 2:
        return None
    a = []
    b = int(math.sqrt(n))
    for i in range(2, n + 1):
        a.append(i)
    for s in range(2, b + 1):
        for x in range(1, len(a)):
            if x < len(a):
                y = a[x]
                if y - s != 0:
                    if y % s == 0:
                        a.remove(y)
    return (a)


def isprime(n):
    if n < 2:
        return None
    x = 0
    for i in range(1, n + 1):
        if n % i == 0:
            x += 1
    if x == 2:
        return True
    else:
        return False


def factorization(n):
    if n < 2:
        return None
    a = []
    x = sieve(n)
    for i in range(0, len(x)):
        y = x[i]
        if n % y == 0:
            e = 1
            n = n / y
            while n % y == 0:
                e += 1
                n = n / y
            a.append([y, e])
    return (a)


def divisornumber(n):
    if n == 1:
        return 1
    elif n < 1:
        return None
    a = 1
    x = factorization(n)
    for i in range(0, len(x)):
        e = x[i][1]
        a = a * (e + 1)
    return (a)


def iscoprime(n, m):
    if n < 1 or m < 1:
        return None
    a = divisornumber(n)
    b = divisornumber(m)
    c = divisornumber(n * m)
    if a * b == c:
        return True
    else:
        return False