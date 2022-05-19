plecak = int(input())
n = int(input())
arr = []
for i in range(n):
    zawartosc = input().split()
    zawartosc[0] = int(zawartosc[0])
    zawartosc[1] = int(zawartosc[1])
    arr.append(zawartosc)

def f(x):
    return x[1] / x[0]

arr.sort(key = f)
print(arr)