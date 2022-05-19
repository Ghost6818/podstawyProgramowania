from math import sqrt
n = int(input())
arr = [True] * (n+1)
def prime(arr, n):
    arr[0] = False
    arr[1] = False
    for i in range (2, int(sqrt(n))+1):
        if arr[i] == True:
            for j in range(i*i, n+1, i):
                arr[j] = False
    return arr
result = prime(arr, n)
for i in range(0,n+1):
    if result[i] == True:
        print(i,end = " ")