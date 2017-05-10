
# written by christoph lueders, chris@cfos.de

def fact2(n):
   """
   Calculate the factorial of n.

   Iterative version.

   >>> fact2(0)
   1
   >>> fact2(3)
   6
   >>> fact2(50)
   30414093201713378043612608166064768844377641568960512000000000000
   """
   assert n >= 0
   r = 1
   for i in range(2, n+1):
      r *= i
   return r

def fact3(n):
   """
   Calculate the factorial of n.

   Divide-and-conquer version.

   >>> fact3(0)
   1
   >>> fact3(3)
   6
   >>> fact3(50)
   30414093201713378043612608166064768844377641568960512000000000000
   """
   assert n >= 0
   return 1 if n < 2 else fact3x(2, n+1)

def fact3x(a, b):
   """
   Helper function to fact3():
   Calculate the product of numbers from a * ... * (b-1)
   """
   assert a < b
   if b-a == 1:
      return a
   if b-a == 2:
      return a * (a+1)
   half = a + (b-a) // 2
   return fact3x(a, half) * fact3x(half, b)


if __name__ == "__main__":
   import doctest
   doctest.testmod()
