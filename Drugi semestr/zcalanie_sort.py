arr = [9, 1, 2, 7, 3, 5, 8, 7]
def merge(arr):
    if len(arr) > 1:
        s = len(arr)//2
        left = arr[:s]
        right = arr[s:]
        merge(left)
        merge(right)
        m(arr,left,right)

def m(arr, l, r):
    print(l,r)
    i_l = i_r = i = 0
    while i_l < len(l) and i_r < len(r):
        if l[i_l] < r[i_r]:
            arr[i] = l[i_l]
            i_l += 1
        else:
            arr[i] = r[i_r]
            i_r += 1
        i += 1
    while i_l < len(l):
        # dodajemy l[i-l] do arr
        arr[i] = l[i_l]
        i += 1
        i_l += 1
    while i_r < len(r):
        arr[i] = r[i_r]
        i += 1
        i_r += 1
merge(arr)
print(arr)
