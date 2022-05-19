from math import sqrt
def sprawdzam(n):
    isPrime = True
    for i in range (2, int(sqrt(n))+1):
        if n% i == 0:
            isPrime = False
    return isPrime
def prime(a):
    arr =[]
    j = 2
    while a > len(arr):
        if sprawdzam(j) == True:
            arr.append(j)
        j += 1
    return arr
a = int(input())
print(prime(a))