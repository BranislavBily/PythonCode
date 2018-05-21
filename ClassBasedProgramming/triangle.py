# print a nice triangle, the triangle has sides the same lenght

import math

class Triangle:
    def __init__(self, hypotenuse):
        self.hypotenuse = hypotenuse
        self.side = 0
        self.surface = 0

    def calculateSide(self):
        self.side = round(math.sqrt(pow(self.hypotenuse, 2) / 2))

    def calculateSurface(self):
        self.surface = round(self.side * self.side / 2)

    def art(self):
        for i in range(1, int(round(self.side + 1))):
            for j in range(0, i):
                print '*',
            print ''


triangle = Triangle(5.656852)
triangle.calculateSide()
triangle.calculateSurface()
print 'Side {0}, surface {1} '.format(triangle.side, triangle.surface)
triangle.art()


