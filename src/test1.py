
firstList=[]
secondList=[]
result=[[0]*5 for _ in range(5)]

a1=[11,12,13,14,15]
a2=[23,45,54,12,23]
for j in range(1,6):
    b=[i*j for i in a1]
    firstList.append(b)
    b=[i*j for i in a2]
    secondList.append(b)

for i in range(len(firstList)):
    for j in range(len(secondList)):
        result[i][j] = firstList[i][j]+secondList[i][j]

print(firstList)
print(secondList)
print(result)