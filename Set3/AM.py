# input numbers into A[3][3] array, print AM

summed, AM = 0, 0
rows, cols = 3, 3

while True:
    A = [[0 for i in xrange(rows)] for i in xrange(cols)]
    for i in range(len(A)):
        for j in range(len(A[i])):
            inputNumber = input('Input your number: ')
            A[i][j] = inputNumber
            summed += inputNumber
    AM = summed / (rows * cols)
    print 'Sum of all numbers {0}, AM is {1}'.format(summed, AM)
    print A






