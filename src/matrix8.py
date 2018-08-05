
def matrix_mul(a, b):
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

a = [[3,2], [4,5]]
b = [[1,-1], [-2, -3]]
r = [[-1,-9], [-6,-19]]
c = matrix_mul(a, b)
for i in range(len(c)):
   for j in range(len(c[0])):
      print(c[i][j],end=" ")
   print()
print("{}  *  {}  =  {}".format(a, b, c))