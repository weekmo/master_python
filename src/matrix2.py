
def matrix_get_submatrix(m,i,j):
    '''
    >>> matrix_get_submatrix([[1,2,3,4],[5,6,7,8],[2,6,4,8],[3,1,1,2]],0,3)
    [[5, 6, 7], [2, 6, 4], [3, 1, 1]]
    '''
    d=len(m)
    assert d>2
    ks=[]
    for x in range(d):
        sub_matrix=[]
        for y in range(d):
            if x !=i and y!=j:
                sub_matrix.append(m[x][y])
        if sub_matrix:
            ks.append(sub_matrix)
    return ks
#Function to Get determinat
def matrix_det2(m):
    '''
    >>> matrix_det2([[1,2,3,4],[5,6,7,8],[2,6,4,8],[3,1,1,2]])
    72
    >>> matrix_det2([[1,2,3,4],[5,7,9,6],[4,6,8,3],[2,5,1,5]])
    77
    >>> matrix_det2([[1,2],[5,6]])
    -4
    '''
    assert isinstance(m,list)
    if isinstance(m[0],list):
        assert len(m)==len(m[0])

    matrix_len=len(m)
    if matrix_len<2:
        return m[0]
    elif matrix_len==2:
        return (m[0][0]*m[1][1])-(m[0][1]*m[1][0])
    else:
        sign=1
        x=0
        for i in range(matrix_len):
            x += sign * m[0][i] * matrix_det2(matrix_get_submatrix(m,0,i))
            sign *= -1
        return x

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(matrix_det2([[1,2,3,4],[5,6,7,8],[2,6,4,8],[3,1,1,2]]))
    print(matrix_det2([2]))
    print(matrix_det2([[3,4,5],[2,1,6],[3,0,-2]]))