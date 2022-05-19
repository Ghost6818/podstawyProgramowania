# arr = [-2,16,4,5,-1,-128,-2]
# size = len(arr)
# print("Przed sortowaniem:", arr)
# for i in range(size):
#     for j in range(0, size-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#             print(arr)
# print("Po sortowaniu:", arr)

def merge(arr, left, right):
    i_left = 0
    i_right = 0
    i = 0
    while i_left < len(left) and i_right < len(right):
        if left[i_left] > right[i_right]:
            arr[i] = left[i_left]
            i_left += 1
        else:
            arr[i] = right[i_right]
            i_right += 1
        i += 1
    while i_left < len(left):
        arr[i] = left[i_left]
        i += 1
        i_left += 1
    while i_right < len(right):
        arr[i] = right[i_right]
        i += 1
        i_right += 1

def m_sort(arr):
    if len(arr) > 1:
        s = len(arr) // 2
        left = arr[:s]  # to samo będzie, gdy napiszemy: tab[:s]
        right = arr[s:]  # to samo będzie, gdy napiszemy: tab[s:]
        m_sort(left)
        m_sort(right)
        merge(arr, left, right)


arr = []
uczniowie = []
sr = []
kl = []
n = int(input())
for i in range(n):
    tab = []
    arr.append(tab)
    print(arr)
    print('hi')
    c = True
    while c == True:
        a = input()
        if a != str('-'):
            # tab.append(a)
            kl = a.split()
            uczniowie.append(kl[0] and kl[1])
            sr.append(kl[-1])
            print(kl)
        if a == str('-'):
            m_sort(sr)
            print(sr)
            x = len(sr)
            y = len(sr) % 10
            for i in range(y):
                print(sr[i])
            c = False