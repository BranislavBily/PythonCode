# 2 inputs of 2 legs of right triangle, calculate hypotenuse, surface and circumference. Do this 10 times
import math


def pythagoreanTheoreum(a, b):
    return round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)


def circumference(a, b, c):
    return round(a + b + c, 2)


def surface(a, b):
    return round(a * b / 2, 2)


repetitions = 0

while repetitions < 10:
    sideA = float(input('Input A side of triangle: '))
    sideB = float(input('Input B side of triangle: '))
    hypotenuse = pythagoreanTheoreum(sideA, sideB)
    print ('Hypotenuse %r , circumference %r , surface %r'
    % (hypotenuse, circumference(sideA, sideB, hypotenuse), surface(sideA, sideB)))
    repetitions += 1

