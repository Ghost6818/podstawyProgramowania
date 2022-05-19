arr=[]
for i in range(10):
    a = int(input())
    arr.append(a)
def minmax(arr):
    arr_min = []
    arr_max = []
    for i in range(0, len(arr) - 1, 2):
        if arr[i] > arr[i + 1]:
            arr_max.append(arr[i])
            arr_min.append(arr[i + 1])
        else:
            arr_max.append(arr[i + 1])
            arr_min.append(arr[i])
    return arr_min, arr_max


def maxymalna(arr):
    maximum = arr[0]
    for n in arr:
        if n > maximum:
            maximum = n
    return maximum


def minimalna(arr):
    minimum = arr[0]
    for n in arr:
        if n < minimum:
            minimum = n
    return minimum


arr_min, arr_max = minmax(arr)
print(arr_min, arr_max)
result = maxymalna(arr_max)
print(result)
result = minimalna(arr_min)
print(result)
print(arr)