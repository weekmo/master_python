
# written by christoph lueders, chris@cfos.de

"""
Our litte library of matrix functions (including ex. sheet 6).

B-IT Master Life Science Informatics
Lab Course: Programming Lab I
Winter term 2016/17
"""

class MatrixException(Exception):
   pass


def matrix_add(a, b):
   """
   Add two matrices.

   Matrices are represented as nested lists, saved row-major.

   >>> matrix_add([[1,1],[2,2]], [[0,-2],[3,9]])
   [[1, -1], [5, 11]]
   >>> matrix_add([[2,3],[5,7]], [[11,13],[17,19]])
   [[13, 16], [22, 26]]
   >>> matrix_add([[2,3,4],[5,7,4]], [[11,13,1],[17,19,1]])
   [[13, 16, 5], [22, 26, 5]]
   """
   rows = len(a)     # number of rows
   cols = len(a[0])  # number of cols
   if rows != len(b) or cols != len(b[0]):
      raise MatrixException("matrices need to have equal dimensions")
   return [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]


def matrix_sub(a, b):
   """
   Subtract two matrices.

   Matrices are represented as nested lists, saved row-major.

   >>> matrix_sub([[1,1],[2,2]], [[0,-2],[3,9]])
   [[1, 3], [-1, -7]]
   >>> matrix_sub([[2,3,4],[5,7,4]], [[11,13,1],[17,19,1]])
   [[-9, -10, 3], [-12, -12, 3]]
   """
   rows = len(a)     # number of rows
   cols = len(a[0])  # number of cols
   if rows != len(b) or cols != len(a[0]):
      raise MatrixException("matrices need to have equal dimensions")
   return [[a[i][j] - b[i][j] for j in range(cols)] for i in range(rows)]


def matrix_mul(a, b):
   """
   Multiply two matrices.

   Matrices are represented as nested lists, saved row-major.

   If A is m x n and B is r x s, the result will be m x s,
   where n == r.

   >>> matrix_mul([[3,2], [4,5]], [[1,-1], [-2,-3]])
   [[-1, -9], [-6, -19]]
   >>> matrix_mul([[2,0,-1], [3,4,5]], [[4,1], [5,0], [-2,-1]])
   [[10, 3], [22, -2]]
   >>> matrix_mul([[2,0,-1,2], [3,4,5,-1], [1,2,6,0]],
   ... [[4,1], [5,0], [-2,-1], [-3,0]])
   [[4, 3], [25, -2], [2, -5]]
   """
   m = len(a)     # number of rows of A
   n = len(a[0])  # number of cols of A
   r = len(b)     # number of rows of B
   s = len(b[0])  # number of cols of B
   if n != r:
      raise MatrixException("matrices need to have compatible dimensions")
   c = [[0] * s for _ in range(m)]   # allocate empty result
   # cycle over all the rows of C (== rows of A)
   for i in range(m):
      # then, cycle over all the cols of C (== cols of B)
      for j in range(s):
         for k in range(n):
            c[i][j] += a[i][k] * b[k][j]
   return c


def matrix_id(d):
   """
   Identity matrix of dimension d.

   Matrices are represented as nested lists, saved row-major.
   Returns a d x d matrix, where all is zero, but the diagonal is 1.

   >>> matrix_id(2)
   [[1, 0], [0, 1]]
   >>> matrix_id(1)
   [[1]]
   >>> matrix_id(3)
   [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
   """
   return [[int(i == j) for j in range(d)] for i in range(d)]


def matrix_transpose(a):
   """
   Return the transpose of a matrix.

   Matrices are represented as nested lists, saved row-major.
   If A is m x n, then the result will be n x m and the contents
   are mirrored on the main diagonal.

   >>> matrix_transpose([[3,2], [4,5]])
   [[3, 4], [2, 5]]
   >>> matrix_transpose([[1,2,3,4], [5,6,7,8]])
   [[1, 5], [2, 6], [3, 7], [4, 8]]
   """
   m = len(a)     # number of rows of A
   n = len(a[0])  # number of cols of A
   return [[a[j][i] for j in range(m)] for i in range(n)]


def matrix_scalar_mul(a, c):
   """
   Multiply the matrix a by a scalar c and return that.

   Matrices are represented as nested lists, saved row-major.

   >>> matrix_scalar_mul([[3,2], [4,5]], 2)
   [[6, 4], [8, 10]]
   >>> matrix_scalar_mul([[1,2,3,4], [5,6,7,8]], -2)
   [[-2, -4, -6, -8], [-10, -12, -14, -16]]
   """
   return [[c * e for e in r] for r in a]


def matrix_get_submatrix(m, ii, jj):
   """
   Return the submatrix of m, where row ii and column jj have been removed.

   Matrices are represented as nested lists, saved row-major.

   >>> matrix_get_submatrix([[1,2],[3,4]],0,0)
   [[4]]
   >>> matrix_get_submatrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],1,1)
   [[1, 3], [7, 9], [10, 12]]
   """
   rows = len(m)     # number of rows of m
   cols = len(m[0])  # number of cols of m
   assert ii >= 0
   assert ii < rows
   assert jj >= 0
   assert jj < cols
   r = []
   for i in range(rows):
      if i != ii:
         r.append([e for j,e in enumerate(m[i]) if j != jj])
   return r


def matrix_det(m):
   """
   Calculate the determinant of a square matrix.

   >>> matrix_det([[12]])
   12
   >>> matrix_det([[1,2],[3,4]])
   -2
   >>> matrix_det([[1,2,3],[4,5,6],[7,8,9]])
   0
   """
   rows = len(m)     # number of rows of m
   assert rows > 0
   cols = len(m[0])  # number of cols of m
   if rows != cols:
      raise MatrixException("matrix has to be square")
   if rows == 1:
      return m[0][0]
   elif rows == 2:
      return m[0][0] * m[1][1] - m[0][1] * m[1][0]
   sgn = 1
   sum = 0
   for i,row in enumerate(m):
      sum += sgn * row[0] * matrix_det(matrix_get_submatrix(m, i, 0))
      sgn *= -1
   return sum


import random
def matrix_rand(rows,cols):
   """
   Generate a random matrix with rows x cols elements,
   where all elements are from [-99,99].
   """
   return [[random.randint(-99,99) for _ in range(cols)] for _ in range(rows)]


def matrix_get_part(m, i, j, a, b):
   """
   Given matrix m, return the submatrix containing rows [i, i+a-1]
   and columns [j, j+b-1].

   Matrices are represented as nested lists, saved row-major.

   >>> matrix_get_part([[1,2],[3,4]], 0,0,1,1)
   [[1]]
   >>> matrix_get_part([[1,2],[3,4]], 0,0,2,2)
   [[1, 2], [3, 4]]
   >>> matrix_get_part([[1,2],[3,4]], 1,1,1,1)
   [[4]]
   >>> matrix_get_part([[1,2],[3,4]], 0,0,2,1)
   [[1], [3]]
   """
   rows = len(m)     # number of rows of m
   cols = len(m[0])  # number of cols of m
   assert i >= 0
   assert a > 0
   assert i+a-1 < rows
   assert j >= 0
   assert b > 0
   assert j+b-1 < cols
   return [[m[i][j] for j in range(j, j+b)] for i in range(i, i+a)]


def matrix_set_part(m, ii, jj, n):
   """
   Given matrix m, replace the submatrix starting at row i, column j
   with the matrix n.

   Matrices are represented as nested lists, saved row-major.

   >>> matrix_set_part([[1,2],[3,4]],0,0,[[9]])
   [[9, 2], [3, 4]]
   >>> matrix_set_part([[1,2],[3,4]],1,1,[[9]])
   [[1, 2], [3, 9]]
   >>> matrix_set_part([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],0,0,[[-1,-2]])
   [[-1, -2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
   >>> matrix_set_part([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],0,0,[[-1],[-2]])
   [[-1, 2, 3], [-2, 5, 6], [7, 8, 9], [10, 11, 12]]
   """
   rows = len(m)     # number of rows of m
   cols = len(m[0])  # number of cols of m
   nrows = len(n)     # number of rows of n
   ncols = len(n[0])  # number of cols of n
   assert ii >= 0
   assert jj >= 0
   assert ii+nrows <= rows
   assert jj+ncols <= cols
   return [[n[i-ii][j-jj] if i >= ii and i < ii+nrows and j >= jj and j < jj+ncols else m[i][j] for j in range(cols)] for i in range(rows)]


def matrix_strassen_mul(a, b, xover=64):
   """
   Given matrices a and b, multiply them by
   Strassen's recursive multiplication algorithm.

   a and b must be square, of same size and of their dimension
   should contain a high power of 2 for the speed-up to be noticeable.

   >>> matrix_strassen_mul([[1,2],[3,4]], [[5,6],[7,8]], xover=1)
   [[19, 22], [43, 50]]
   >>> matrix_strassen_mul([[1,2,9,8],[3,4,-1,-2],[8,4,2,9],[7,6,5,4]], [[5,6,0,1],[7,8,-1,-2],[-1,-2,-3,9],[5,4,3,1]], xover=1)
   [[50, 36, -5, 86], [34, 44, -7, -16], [111, 112, 17, 27], [92, 96, -9, 44]]
   >>> a = matrix_rand(16,16)
   >>> b = matrix_rand(16,16)
   >>> matrix_mul(a,b) == matrix_strassen_mul(a,b,xover=1)
   True
   """
   arows = len(a)     # number of rows of a
   acols = len(a[0])  # number of cols of a
   brows = len(b)     # number of rows of b
   bcols = len(b[0])  # number of cols of b
   if arows != acols or brows != bcols or arows != brows or arows % 2 != 0 or arows < xover:
      # not square or not same dimensions or not divisible by 2 or below crossover
      return matrix_mul(a,b)
   half = arows // 2
   # get sub-matrices
   a11 = matrix_get_part(a, 0, 0, half, half)
   a12 = matrix_get_part(a, 0, half, half, half)
   a21 = matrix_get_part(a, half, 0, half, half)
   a22 = matrix_get_part(a, half, half, half, half)
   b11 = matrix_get_part(b, 0, 0, half, half)
   b12 = matrix_get_part(b, 0, half, half, half)
   b21 = matrix_get_part(b, half, 0, half, half)
   b22 = matrix_get_part(b, half, half, half, half)
   # calculate intermediate matrices
   m1 = matrix_strassen_mul(matrix_add(a11, a22), matrix_add(b11, b22))
   m2 = matrix_strassen_mul(matrix_add(a21, a22), b11)
   m3 = matrix_strassen_mul(a11, matrix_sub(b12, b22))
   m4 = matrix_strassen_mul(a22, matrix_sub(b21, b11))
   m5 = matrix_strassen_mul(matrix_add(a11, a12), b22)
   m6 = matrix_strassen_mul(matrix_sub(a21, a11), matrix_add(b11, b12))
   m7 = matrix_strassen_mul(matrix_sub(a12, a22), matrix_add(b21, b22))
   # combine
   c11 = matrix_add(matrix_add(m1, m4), matrix_sub(m7, m5))
   c12 = matrix_add(m3, m5)
   c21 = matrix_add(m2, m4)
   c22 = matrix_add(matrix_sub(m1, m2), matrix_add(m3, m6))
   # build result
   r = [c11[i] + c12[i] for i in range(half)] + [c21[i] + c22[i] for i in range(half)]
   return r


if __name__ == "__main__":
   import doctest
   doctest.testmod()
