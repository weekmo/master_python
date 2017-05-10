import matrix1 as mx
import math as m
def matrix_sub(a, b):
    '''
    >>> matrix_sub([[2,4,6,8],[10,14,18,12],[8,12,16,6],[4,10,2,10]],[[1,2,3,4],[5,7,9,6],[4,6,8,3],[2,5,1,5]])
    [[1, 2, 3, 4], [5, 7, 9, 6], [4, 6, 8, 3], [2, 5, 1, 5]]
    '''
    rows = len(a)
    cols = len(a[0])
    return [[a[i][j] - b[i][j] for j in range(cols)] for i in range(rows)]

def matrix_get_part(m,i,j,a,b):
    '''
    >>> matrix_get_part([[1,16,-8,-24,6,5,6,7],[0,7,-87,7,8,3,3,8],[71,-76,5,4,-1,8,2,6],[-27,63,-5,2,-72,-2,7,8],[46,7,8,6,4,75,2,4],[8,47,64,8,87,-8,7,2],[0,7,-87,7,8,3,3,8],[-27,63,-5,2,-72,-2,7,8]],0,1,3,4)
    [[16, -8, -24], [7, -87, 7], [-76, 5, 4]]
    '''
    result=[]
    for x in range(i,a):
        sub_mat=[]
        for y in range(j,b):
            sub_mat.append(m[x][y])
        result.append(sub_mat)
    return result

def matrix_mul_strassen(a,b):
    '''
    >>> mat1=[[1,2,3,4],[5,7,9,6],[4,6,8,3],[2,5,1,5]]
    >>> matrix_mul_strassen(mat1,mat1)
    [[31, 54, 49, 45], [88, 143, 156, 119], [72, 113, 133, 91], [41, 70, 64, 66]]
    '''

    n = len(a)
    half=n//2
    assert (m.log(len(a),2)).is_integer()
    assert (m.log(len(b),2)).is_integer()
    if n <= 2:
        return mx.matrix_mul(a, b)
    else:
        #dividing the matrices in 4 sub-matrices:
        a11= matrix_get_part(a,0,0,half,half)
        a12=matrix_get_part(a,0,half,half,n)
        a21=matrix_get_part(a,half,0,n,half)
        a22=matrix_get_part(a,half,half,n,n)

        b11= matrix_get_part(b,0,0,half,half)
        b12=matrix_get_part(b,0,half,half,n)
        b21=matrix_get_part(b,half,0,n,half)
        b22=matrix_get_part(b,half,half,n,n)

        # Calculating m1 to m7:
        a_result = mx.matrix_add(a11,a22)
        b_result = mx.matrix_add(b11,b22)
        m1 = matrix_mul_strassen(a_result, b_result) # m1 = (a11+a22) * (b11+b22)

        a_result = mx.matrix_add(a21, a22)      # a21 + a22
        m2 = matrix_mul_strassen(a_result, b11)  # m2 = (a21+a22) * (b11)

        b_result = matrix_sub(b12, b22) # b12 - b22
        m3 = matrix_mul_strassen(a11, b_result)  # m3 = (a11) * (b12 - b22)

        b_result = matrix_sub(b21, b11)
        m4 =matrix_mul_strassen(a22, b_result)   # m4 = (a22) * (b21 - b11)

        b_result = mx.matrix_add(a11, a12)      # a11 + a12
        m5 = matrix_mul_strassen(b_result, b22)  # m5 = (a11+a12) * (b22)

        a_result = matrix_sub(a21, a11) # a21 - a11
        b_result = mx.matrix_add(b11, b12)      # b11 + b12
        m6 = matrix_mul_strassen(a_result, b_result) # m6 = (a21-a11) * (b11+b12)

        a_result = matrix_sub(a12, a22) # a12 - a22
        b_result = mx.matrix_add(b21, b22)  # b21 + b22
        m7 = matrix_mul_strassen(a_result, b_result) # m7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
        a_result = mx.matrix_add(m1, m4) # m1 + m4
        b_result = matrix_sub(m5, m7) # m1 + m4 + m7
        c11 = matrix_sub(a_result, b_result) # c11 = m1 + m4 - m5 + m7

        c12 = mx.matrix_add(m3, m5) # c12 = m3 + m5
        c21 = mx.matrix_add(m2, m4)  # c21 = m2 + m4

        a_result = matrix_sub(m1, m2) # m1 + m3
        b_result = mx.matrix_add(m3, m6) # m1 + m3 + m6
        c22 = mx.matrix_add(a_result, b_result) # c22 = m1 + m3 - m2 + m6

        # Grouping the results obtained in a single matrix:
        result = [[0 for j in range(n)] for i in range(n)]
        for i in range(half):
            for j in range(half):
                result[i][j] = c11[i][j]
                result[i][j + half] = c12[i][j]
                result[i + half][j] = c21[i][j]
                result[i + half][j + half] = c22[i][j]
        return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    mat1=[[1,2,3,4],[5,7,9,6],[4,6,8,3],[2,5,1,5]]
    mat2=[[1,2,3],[5,7,9],[4,6,8]]
    mat5=[[1,16,-8,-24,6,5,6,7],[0,7,-87,7,8,3,3,8],[71,-76,5,4,-1,8,2,6],[-27,63,-5,2,-72,-2,7,8],[46,7,8,6,4,75,2,4],[8,47,64,8,87,-8,7,2],[0,7,-87,7,8,3,3,8],[-27,63,-5,2,-72,-2,7,8]]
    print(matrix_mul_strassen(mat1,mat1))
    print(matrix_mul_strassen(mat5,mat5))