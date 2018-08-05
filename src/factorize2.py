def erathostenes(max):
    prims = []
    mark = [False] * max  # initialize marks
    for i in range(2, max):
        if not mark[i]:
            prims.append(i)
            # not marked, i.e. prime
            for j in range(i * i, max, i):
                # mark all multiples of i
                mark[j] = True
    return prims

def factorize(n):
    prims = erathostenes(n)
    facts=[]
    dictionary={}
    for j in prims:
        if n%j==0:
            facts.append(j)
            n //=j
    print(prims)
    print(facts)
    for i in facts:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    print(dictionary)

factorize(12)
    #print(facts)