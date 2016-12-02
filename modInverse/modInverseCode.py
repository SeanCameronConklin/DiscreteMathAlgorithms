import math
import numpy
play = True
def modInverse(x, y):
    origX = x
    origY = y
    while y != 0:
        z = x % y
        x = y
        y = z
        gcdValue = x
    print('The Eucilidean Algorithm suggests that the GCD is', gcdValue)
    x = origX
    y = origY
    i = 1
    j = 1
    multX = x * i
    multY = y * j
    while multX <= x * y and multY <= x * y and (multY - multX) != gcdValue:
        if multX <= multY:
            i += 1
            multX = x * i
            multY = y * j
        else:
            j += 1
            multX = x * i
            multY = y * j
    modInvVal = y - i
    print('The inverse of', x, "mod", y, "is:", modInvVal)
while play:
    print()
    print("The formula for this code is: inverse of x mod y")
    print()
    a = int(input("Input an x value: "))
    b = int(input("Input a y value: "))
    print()
    modInverse(a, b)

