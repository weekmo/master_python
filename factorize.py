import time
def factorize(n):
    primset = []
    div_value = 2
    while div_value*div_value <= n:
        while (n % div_value) == 0:
            primset.append(div_value)
            n //= div_value
        div_value += 1
    if n > 1:
        primset.append(n)
    return {i:primset.count(i) for i in primset}

print(factorize(100))

'''x=time.perf_counter()
factorize(0)
y=time.perf_counter()
print(y-x)'''

