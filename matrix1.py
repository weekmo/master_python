
'''
>>> matrix_id(3)
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
>>> matrix_id(1)
[1]
>>> matrix_transpose([[1,3,5],[2,4,6]])
[[1, 2], [3, 4], [5, 6]]
>>> matrix_transpose([1,2,5])
[[1], [2], [5]]
>>> matrix_transpose([[1],[2],[5]])
[1, 2, 5]
>>> matrix_transpose([5])
[5]
>>> matrix_transpose([])
[]
>>> matrix_transpose([[]])
[]
>>> matrix_transpose([[],[]])
[]
>>> matrix_scalar_mul([[1,-1,-3],[0,0,-6]],-2)
[[-2, 2, 6], [0, 0, 12]]
>>> matrix_scalar_mul([1,-1,-3],-2)
[-2, 2, 6]
>>> matrix_scalar_mul([[1],[-1],[-3],[-2]],-2)
[[-2], [2], [6], [4]]
>>> matrix_scalar_mul([-1],-2)
[2]
>>> matrix_scalar_mul([[],[]],-2)
[[], []]
>>> matrix_scalar_mul([[]],-2)
[[]]
>>> matrix_scalar_mul([],-2)
[]
'''
#Get identity matrix function
def matrix_id(dimention):
    assert dimention>0
    if dimention==1:
        return [1]
    matrix = [[0] * dimention for _ in range(dimention)]

    for i in range(dimention):
        for j in range(dimention):
            matrix[i][i]=1
    return matrix

#transpose matrix function

def matrix_transpose(matrix):
    if len(matrix)<=0:
        return matrix
    new_matrix_rows=len(matrix)
    new_matrix=[]
    if isinstance(matrix[0],list):
        new_matrix_columns=len(matrix[0])
        if new_matrix_columns==1:
            for i in matrix:
                for j in i:
                    new_matrix.append(j)
        else:
            new_matrix=[[0]*new_matrix_rows for _ in range(new_matrix_columns)]
            for i in range(new_matrix_columns):
                for j in range(new_matrix_rows):
                    new_matrix[i][j]=matrix[j][i]
    elif new_matrix_rows>1:
        for i in range(new_matrix_rows):
            new_matrix.append([matrix[i]])
    elif new_matrix_rows == 1 :
        return matrix
    return new_matrix

#Multiply matrix with a number
def matrix_scalar_mul(matrix,scal):
    if len(matrix)<=0:
        return []
    matrix_rows=len(matrix)
    if isinstance(matrix[0],list):
        matrix_column=len(matrix[0])
        for i in range(len(matrix)):
            for j in range(matrix_column):
                matrix[i][j]*=scal
    else:
        for i in range(matrix_rows):
            matrix[i]*=scal
    return matrix


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Identity Matrix Function results")
    print(matrix_id(1))
    print(matrix_id(5))
    print()
    print("Transpose Matrix Function results")
    print(matrix_transpose([[1,2,5],[3,4,6]]))
    print(matrix_transpose([1,2,5]))
    print(matrix_transpose([[1],[2],[5]]))
    print(matrix_transpose([1]))
    print(matrix_transpose([]))
    print()
    print("Scale Matrix Function results")
    print(matrix_scalar_mul([[1,-1,-3],[0,0,-6]],-2))
    print(matrix_scalar_mul([1,-1,-3],-2))
    print(matrix_scalar_mul([[1],[-1],[-3],[-2]],-2))
    print(matrix_scalar_mul([-1],-2))
    print(matrix_scalar_mul([[],[]],-2))
