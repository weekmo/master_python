'''def erathostenes(max):
    mark = [True] * max  # initialize marks
    for i in range(2, max):
        if mark[i]:
            yield i
            # not marked, i.e. prime
            for j in range(i * i, max, i):
                # mark all multiples of i
                mark[j] = False
'''
def erathostenes(max):
    prims=[]
    mark = [False] * max  # initialize marks
    for i in range(2, max):
        if not mark[i]:
            prims.append(i)
            # not marked, i.e. prime
            for j in range(i * i, max, i):
                # mark all multiples of i
                mark[j] = True
    return  prims

def factorize(n):
    if n < 2: return []
    primes = erathostenes(int(n ** 0.5) + 1)
    facts = []

    for prim in primes:
        if prim * prim > n: break
        while n % prim == 0:
            facts.append(prim)
            n //= prim
    if n > 1: facts.append(n)

    return {i: facts.count(i) for i in facts}

print(factorize(947625138698723668))