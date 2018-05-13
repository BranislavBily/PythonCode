#input integers until the input equals 0, then print biggest number
while True:
    number = 1
    biggestInput = 0
    while number != 0:
        number = int(input('Input your number: '))
        if number > biggestInput:
            biggestInput = number
    print biggestInput
