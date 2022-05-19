from math import sqrt
n = int(input())
isPrime = True
for i in range (2, int(sqrt(n))+1):
    if n% i == 0:
        isPrime = False
if isPrime :
    print('is prime')
else:
    print('not prime')