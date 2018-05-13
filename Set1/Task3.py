#generate 10 numbers from <0, 20> and print Arithetic mean

import random

AM, sum = 0, 0
for i in range (10):
    number = random.uniform(0, 20)
    sum += number
AM = round(sum / 10, 2)
print AM
