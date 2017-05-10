import math


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x * 1.0
        self.y = y * 1.0
        self.z = z * 1.0

    def update(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def normalize(self):
        lenghth = self.length()
        self.x /= lenghth
        self.y /= lenghth
        self.z /= lenghth

    def length(self):
        return (self.x ** 2.0 + self.y ** 2.0 + self.z ** 2.0) ** 0.5

    def printVec(self):
        print(self.x, self.y, self.z)

    def increament(self, vec):
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __getitem__(self, item):
        if item==0:
            return self.x
        elif item ==1:
            return self.y
        elif item ==2:
            return self.z
        else:
            raise IndexError("index out of range")
    def __iadd__(self, other):
        return self.__add__(other)
    def __str__(self):
        return self.printVec()


x = Vector()
y = Vector(1, 2, 3)
x.update(1, 2, 3)
x.normalize()
x.printVec()
x.increament(y)
x.printVec()
z = x + y
z.printVec()
z = x - y
z.printVec()
print(y * x)
print(z[0],z[2],z[1])
print("---------------------------------")
x.printVec()
z.printVec()
z+=x
z.printVec()
print(z)
