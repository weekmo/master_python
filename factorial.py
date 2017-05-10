'''
>>> fact2(5)
120
>>> fact2(0)
1
>>> fact2(1)
1
>>> fact3(5)
120
>>> fact3(0)
1
>>> fact3(1)
1
'''


# Iterative factorial
def fact2(n):
    assert n >= 0
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#Recursive factorial
def fact_calculator(n, m):
    if n == m:
        return n
    else:
        if m > n:
            return 1
        if n == m + 1:
            return n * m
        else:
            return fact_calculator(n, (n + m) // 2) * fact_calculator(((n + m) // 2) - 1, m)


def fact3(n):
    return fact_calculator(n, 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(fact2(6))
    print(fact2(0))
    print(fact2(1))
    print(fact3(6))
    print(fact3(0))
    print(fact3(1))


