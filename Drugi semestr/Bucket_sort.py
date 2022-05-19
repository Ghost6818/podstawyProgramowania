def backet_sort(arr,bt):
    p = []
    for i in range(bt):
        bts = []
        p.append(bts)
    tab = []
    for i in range(len(arr)):
        tab.append(arr[i][1])
    for i in range(len(arr)):
        if arr[i][1] == max(tab):
            p[bt-1].append(arr[i])
        else:
            s = (arr[i][1] - min(tab)) // (max(tab)/bt)
            p[int(s)].append(arr[i])
    for i in range(bt):
        p[i].sort(key=fun)
    l = []
    for n in p:
        for j in n:
            l.append(j)
    return l
def fun(x):
    return x[1]

arr = []
p = []
p = input().split()
p[0] = int(p[0])
p[1] = int(p[1])

for i in range(p[1]):
    n = int(input())

    for j in range(n):
        o = input().split()
        o[0] = int(o[0])
        o[1] = float(o[1])
        arr.append(o)
    arr = backet_sort(arr,3)
    li = arr[:5]
    arr = arr[5:]
    for k in li:
        print(k[0], end = ' ')
    print()
