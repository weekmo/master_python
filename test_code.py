'''
It is a wrong way because we append the same row many times,
That means we pass the row by reference and we chan
'''
c=[0]*5
mat=[]
for i in range(3):
    mat.append(c)
mat[0][0]=5
mat[1][3]=9
print(mat)
