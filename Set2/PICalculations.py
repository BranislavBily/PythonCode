# input radius and calculate circumference, surface, volume of circle and sphere respectively

import math


def circumference():
    return round(math.pi * 2 * radius, 2)


def circleSurface():
    return round(pow(radius, 2) * math.pi, 2)


def sphereSurface():
    return round(4 * math.pi * pow(radius, 2), 2)


def sphereVolume():
    return round(4 * math.pi * pow(radius, 3) / 3, 2)


radius = 1.0
while radius != 0:
    radius = float(input('Input radius: '))
    print('Circumference is %r, surface of circle is %r, surface of sphere is %r, volume of sphere is %r'
          % (circumference(), circleSurface(), sphereSurface(), sphereVolume()))


