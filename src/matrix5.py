import matrix2 as mx


def matrix_inverse(matrix):
    '''
    >>> matrix_inverse([[4, 7], [2, 6]])
    [[0.6, -0.7], [-0.2, 0.4]]
    >>> matrix_inverse([[0.6, -0.7], [-0.2, 0.4]])
    [[4.0, 7.0], [2.0, 6.0]]
    >>> matrix_inverse([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    [[-24.0, 18.0, 5.0], [20.0, -15.0, -4.0], [-5.0, 4.0, 1.0]]
    >>> matrix_inverse([[-24, 18, 5], [20, -15, -4], [-5, 4, 1]])
    [[1.0, 2.0, 3.0], [0.0, 1.0, 4.0], [5.0, 6.0, 0.0]]
    >>> print(matrix_inverse([1]))
    Traceback (most recent call last):
        File "/home/mohammed/IdeaProjects/ex8/first.py", line 61, in <module>
            print(matrix_inverse([1]))
        File "/home/mohammed/IdeaProjects/ex8/first.py", line 16, in matrix_inverse
            assert matrix_length == len(matrix[0])  # Matrix must be square
    TypeError: object of type 'int' has no len()
    >>> print(matrix_inverse([[1,3,5],[7,3,2]]))
    Traceback (most recent call last):
        File "/usr/lib64/python3.4/doctest.py", line 1318, in __run
            compileflags, 1), test.globs)
        File "<doctest __main__.matrix_inverse[5]>", line 1, in <module>
            print(matrix_inverse([[1,3,5],[7,3,2]]))
        File "/home/mohammed/IdeaProjects/ex8/first.py", line 30, in matrix_inverse
            assert matrix_length == len(matrix[0])  # Matrix must be square
    AssertionError
    '''
    matrix_length = len(matrix)  # getting matrix length
    assert matrix_length == len(matrix[0])  # Matrix must be square
    assert mx.matrix_det(matrix) != 0  # Matrix must not be singular
    inversedMatrix = mx.matrix_id(matrix_length)  # Creating Identity Matrix
    [[row2.append(item) for item in row1] for row1, row2 in zip(inversedMatrix, matrix)]  # merge two matrix's
    elementary_row_operation(matrix)  # elementary row operations
    # return inverted matrix
    return [[round(matrix[row][col], 2) for col in range(matrix_length, len(matrix[0]))] for row in
            range(0, len(matrix))]


def elementary_row_operation(a):
    '''
    >>> elementary_row_operation([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    '''
    lead = 0
    rowNum = len(a)
    columnCount = len(a[0])
    for r in range(rowNum):
        if lead >= columnCount:  # it will work for the first part of the matrix only
            break
        i = r
        while a[i][lead] == 0:  # if the first element in the row is 0 we will swap the row
            i += 1
            if i == rowNum:  # if we are in the last row we will shift to the next column
                i = r
                lead += 1
                if columnCount == lead:  # if we reach the beginning of the second part of the matrix we will stop
                    break
        a[i], a[r] = a[r], a[i]  # swapping rows
        lv = a[r][lead]
        a[r] = [mrx / float(lv) for mrx in a[r]]  # divide the row elements to get one
        for i in range(rowNum):
            if i != r:
                lv = a[i][lead]
                a[i] = [iv - lv * rv for rv, iv in zip(a[r], a[i])] # multiply and subtract to get zeros
        lead += 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    b11 = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    c11 = [[-24, 18, 5], [20, -15, -4], [-5, 4, 1]]
    d11 = [[4, 7], [2, 6]]
    e11 = [[0.6, -0.7], [-0.2, 0.4]]

    print(matrix_inverse(b11))
    print(matrix_inverse(c11))
    print(matrix_inverse(d11))
    print(matrix_inverse(e11))
