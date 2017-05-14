import math as mt


def blosum(sequ):
    fa = {j: sum(i.count(j) for i in sequ) for i in sequ for j in i}
    num_lett = sum(i for i in fa.values())
    pa = {k: v / num_lett for k, v in fa.items()}
    fab = {}
    for i in zip(*sequ):
        for j in fa:
            r = i.count(j)
            if r > 1:
                x = r * (r - 1) / 2
                if j + j in fab:
                    fab[j + j] += x
                else:
                    fab[j + j] = x
            for n in fa:
                if j != n:
                    key = "".join(sorted(j + n))
                    o = (i.count(j) * i.count(n)) / 2
                    if o > 0:
                        if key in fab:
                            fab[key] += o
                        else:
                            fab[key] = o
    num_pair = sum(i for i in fab.values())
    pab = {k: v / num_pair for k, v in fab.items()}
    e = {k + v: pa[k] ** 2 if k == v else 2 * pa[k] * pa[v] for k, v in fab}
    sab = {k[0]: round(2 * mt.log2(k[1] / v[1])) for k, v in zip(sorted(pab.items()), sorted(e.items()))}
    matrix = [[0] * (len(fa) + 1) for _ in range(len(fa) + 1)]
    matrix[0][0] = '#'
    for i, v in enumerate(fa.keys()):
        matrix[i + 1][0] = v
        matrix[0][i + 1] = v
        for j, l in enumerate(fa.keys()):
            key="".join(sorted(v+l))
            if key in sab:
                matrix[j + 1][i + 1] = sab[key]
    return matrix
