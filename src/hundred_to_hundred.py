import itertools as it

# Create variables
x = ['+', '-', '/', '*', '']
p = []
r = []
counter = 0
# Create list of numbers and operations
for i in range(1, 10):
    temp = []
    for j in x:
        temp.append(str(i) + j)
    p.append(temp)
#print(p)
# Cartesian products
p = ["".join([i for i in l]) for l in list(it.product(*p))]
# Remove operations from the end of equations
for i in p:
    if not i[-1].isdigit():
        r.append(i[:-1])
    else:
        r.append(i)

r=set(r)
# Print only equations that equals hundred
for i in r:
    res = eval(i)
    if res == 100:
        print(i + " = " + str(res) + "\n")
        counter += 1
print("Total:",counter)
