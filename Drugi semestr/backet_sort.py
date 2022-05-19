arr = [0.5,0.01,0.9,0.99,0.33,0.4,0.6,0.75,0,1]
bt = int(input())
def backet_sort(arr,bt):
    p = []
    for i in range(bt):
        bts = []
        p.append(bts)
    for i in range(len(arr)):
        if arr[i] == max(arr):
            p[bt-1].append(max(arr))
        else:
            s = (arr[i] - min(arr)) // (max(arr)/bt)
            p[int(s)].append(arr[i])
    arr = []
    for i in range(bt):
        p[i].sort()
        for n in range(len(p[i])):
            arr.append(p[i][n])
    print(arr)
backet_sort(arr,bt)