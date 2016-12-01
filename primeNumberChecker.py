import math

# Reference: https://primes.utm.edu/howmany.html

play = True

while play:
    x = int(input("Enter a potential prime integer: "))
    isPrime = False
    i = 1
    count = 0
    maxDiv = math.sqrt(x)
    while maxDiv >= i and count <= 1:
        if x % i == 0:
            count += 1
            i += 1
        else:
            i += 1
    if count <= 1:
        isPrime = True
        print("Is a prime number.")
    else:
        isPrime = False
        print("Is not a prime number.")
