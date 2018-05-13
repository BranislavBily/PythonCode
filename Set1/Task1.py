# input interger, print how many digits are lower than 5
while True:
    number = input('Your number: ')
    amount = 0
    number = float(number)
    while number / 10 > 0.1:
        if number % 10 < 5:
            amount += 1
        number /= 10
    print amount



