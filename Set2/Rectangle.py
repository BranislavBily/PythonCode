# calculate circumference of rectangle from inputs and print if the inputted line will be long enough


def circumference(w, h):
    return round(2 * w + 2 * h, 2)


while True:
    sideA = float(input('Input side A: '))
    sideB = float(input('Input side B: '))
    line = float(input('Input your line: '))
    if line > circumference(sideA, sideB):
        print 'It will be enough'
    else:
        print 'It will not be enough'
