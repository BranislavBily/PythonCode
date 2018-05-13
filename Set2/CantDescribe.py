# if input is positive, calculate factorial of input and sum of numbers <1, number>

factorial, addition = 1, 0

while True:
    number = int(input('Input your number: '))
    if number > 0:
        for i in range(1, number + 1):
            factorial *= i
            addition += i
        print 'Factorial of {0} is {1}, sum of numbers from  to {0} is {2}'.format(number, factorial, addition)
    else:
        print 'Number too low'
