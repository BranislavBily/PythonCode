# calculating serial and parallel resistance of 2 resistors

while True:
    R1 = round(input('Input resistance of R1: '), 2)
    R2 = round(input('Input resistance of R2: '), 2)

    def serial(r1, r2):
        return round(r1 + r2, 2)

    def parallel(r1, r2):
        return round(r1 * r2 / (r1 + r2), 2)
    print "Serial resistance is %d parallel resistance %d" %(serial(R1, R2), parallel(R1, R2))
