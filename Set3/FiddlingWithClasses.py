# input char, find the biggest in ASCII and print where in array it is located

from Point import Point

rows, cols = 3, 3

Points = []

for i in range(4):
    p = Point(i, i * 2)
    Points.append(p)

for i in range(4):
    print Points[i].x, Points[i].y,
