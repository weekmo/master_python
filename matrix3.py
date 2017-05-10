
# written by christoph lueders, chris@cfos.de

"""
Our litte library of matrix functions (including ex. sheet 6).

B-IT Master Life Science Informatics
Lab Course: Programming Lab I
Winter term 2016/17
"""

def matrix_add(a, b):
   """
   Add two matrices.

   Matrices are represented as nested lists, saved row-major.

   >>> matrix_add([[1,1],[2,2]], [[0,-2],[3,9]])
   [[1, -1], [5, 11]]
   >>> matrix_add([[2,3],[5,7]], [[11,13],[17,19]])
   [[13, 16], [22, 26]]
   >>> matrix_add([[2,3,4],[5,7,4]], [[11,13],[17,19]])
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "day-10-matrix-add.py", line 16, in matrix_add
       # then, cycle over all the cols
   IndexError: list index out of range
   >>> matrix_add([[2,3,4],[5,7,4]], [[11,13,1],[17,19,1]])
   [[13, 16, 5], [22, 26, 5]]
   """
   rows = len(a)     # number of rows
   cols = len(a[0])  # number of cols
   return [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]


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
   return [[1 if i == j else 0 for j in range(d)] for i in range(d)]


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
   m = len(a)     # number of rows of A
   n = len(a[0])  # number of cols of A
   return [[c * a[i][j] for j in range(n)] for i in range(m)]


if __name__ == "__main__":
   import doctest
   doctest.testmod()
