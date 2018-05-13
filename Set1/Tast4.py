# input integer and print it in binary

number = int(input("Input a number number:"))
binary = ""
while number > 0:
    binary = str(number % 2) + binary
    number = number / 2
print("Your binary number is: " + binary)
