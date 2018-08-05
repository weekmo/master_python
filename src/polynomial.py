
def poly_norm(a):
   """
   Normalize a polynomial, i.e. remove any leading zero coefficients.

   Works in-place.
   """
   while len(a) > 0:
      if a[-1] == 0:          # instead of a[len(a)-1]
         a.pop()
      else:
         break


def poly_mul(a, b):
   """
   Multiply two polynomials.

   Both polynomials are given as lists of their coefficients.
   Return their normalized product.
   """
   # initialize result poly to zero
   r = [0] * (len(a) + len(b) - 1)
   # cycle through all coeff products
   for i in range(len(a)):
      for j in range(len(b)):
         r[i+j] += a[i] * b[j]
   # normalize
   poly_norm(r)
   return r


def poly_mul2(a, b):
   """
   Multiply two polynomials.

   Both polynomials are given as lists of their coefficients.
   Return their normalized product.
   More pythonic style.
   """
   # initialize result poly to zero
   r = [0] * (len(a) + len(b) - 1)
   # cycle through all coeff products
   for i,aa in enumerate(a):
      for j,bb in enumerate(b):
         r[i+j] += aa * bb
   # normalize
   poly_norm(r)
   return r


    # test leading b coeff zero
