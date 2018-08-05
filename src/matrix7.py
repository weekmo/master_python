
adjacency = [[ 1.,  1.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  0.,  0.,  0.,  1.,  1.,  1.,  1.],
        [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,  0.],
        [ 0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.],
        [ 0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.],
        [ 0.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.],
        [ 0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,  0.],
        [ 1.,  1.,  1.,  0.,  0.,  0.,  1.,  1.,  1.,  1.],
        [ 1.,  1.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  1.]]

adja2 = [[1,1,1,1],
        [1,1,0,1],
        [1,0,1,0],
        [1,1,0,1]]

def matmult(a,b):
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]

def normalizeCol(matrix):
    
    for col in range(len(matrix[0])):
        sum1 = sum(elem[col] for elem in matrix)
        for row in matrix:
            row[col] /= sum1
            row[col] = round(row[col], 2)
    
    return matrix

def inflate(matrix, factor):
    
    for col in range(len(matrix[0])):
        for row in matrix:
            row[col] = row[col] ** factor
        
    return normalizeCol(matrix)

temp = normalizeCol(adjacency)

for _ in range(7):
    temp = inflate(matmult(temp, temp),2)

for each in temp:
    print(each)