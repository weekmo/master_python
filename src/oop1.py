import math
import doctest
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def set_radius(self,radius):
        self.radius = radius

    def area(self):
        """
        >>> circle = Circle(5)
        >>> round(circle.area(),8)
        78.53981634
        """
        return math.pi * self.radius ** 2

    def circumfence(self):
        """
        >>> circle1 = Circle(5)
        >>> round(circle1.circumfence(),9)
        31.415926536
        """
        return 2 * math.pi * self.radius

if __name__=="__main__":
    doctest.testmod()
    circle1 = Circle(5)
    print("Radius 5")
    print("Area:",circle1.area())
    print("Circumference:",circle1.circumfence())
    print()
    circle1.set_radius(9)
    print("Radius 9")
    print("Area:",circle1.area())
    print("Circumference:",circle1.circumfence())
