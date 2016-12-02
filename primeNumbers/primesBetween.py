#Reference: http://mathworld.wolfram.com/PrimeNumberTheorem.html

import math
import numpy

play = True
while play:

    primeCounter = 0
    realNumPrimes = 0
    amount = 1
    yCount = 0
    a = 0
    print()
    x = int(input('Enter the smaller of two numbers: '))
    y = int(input('Enter the larger of two numbers: '))
    amount = int(input('Enter the number of prime numbers to find between the two numbers: '))
    if x == 1:
        primeEst = (y / numpy.log(y))
    else:
        primeEst = (y / numpy.log(y)) - (x / numpy.log(x))
    print()
    print("Given the inputs, the Prime Number Theorem would estimate", int(round(primeEst)), "non-inclusive prime numbers between", x, "and", y)
    print()
    print("Here are up to", amount, "non-inclusive prime numbers between", x, "and", y)
    print ()
    x = x + 1
    while primeCounter < amount:
        count = 0
        i = 1
        maxDiv = math.sqrt(x)
        if x <= y:
            while maxDiv >= i and count <= 1:
                if x % i == 0:
                    count += 1
                    i += 1
                else:
                    i += 1
            if count == 1:
                isPrime = True
                print(x)
                primeCounter += 1
                realNumPrimes = primeCounter
                x += 1
                count = 0
            else:
                isPrime = False
                x += 1
                count = 0
        elif x > y:
            print()
            print("There are", realNumPrimes, "prime numbers between", x, "and", y, "given the condition of finding", amount, "prime numbers.")
            primeCounter = amount
