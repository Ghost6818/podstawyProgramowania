#żeby wynegerować jakąś losową liczbę i do tej liczby znaleźć liczby pierwszej
#następnie znaleźć w tch liczbach pierwszych daną liczbę np. 618
# i wyświetl jej indeks
from math import sqrt
def eratotenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range (2, int(sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j] = False
    primes = []
    for i in range(n):
        if is_prime[i]:
            primes.append(i)
    return primes
tab = [3,14,8,7,12]
a = int(input())
def search(tab,a):
    i = 0
    while i < len(tab):
        i += 1
        if tab[i] == a:
            return i
    return -1
n = 618
x = 331
arr = eratotenes(n)
index = search(arr, x)