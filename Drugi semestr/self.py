# class Product:
#     def __init__(self,name,code):
#         self.name=name
#         self.code=code
# x=int(input())
# arr = []
# list = []
# for i in range(x):
#     y=input().split()
#     arr.append(y)
#     p1=Product(y[0],int(y[1]))
#     list.append(p1)
# for i in range(x):
#     if x == 0 :
#         list.append([arr[i].name[0],i])
#     elif x == 1:
#         print(arr[i].code[0])
#         list.append([arr[i].code[0],i])
#     for z in range(1,len(list)):
#         number = list[z]
#         while x >= 0 and number < list[x]:
#             list[x+1] = number
#             x = x - 1
#         list[x+1] = number
#         for x in range(x):
#             print(arr[list[x][1]].name,arr[list[x][1]].code)
#
#

x = int(input())
arr = []
def sort(arr):
    y = int(input())
    if y == 1:
        for i in range(1, len(arr)):
            s = arr[i]
            n = i - 1
            while n >= 0 and s[1] > arr[n][1]:
                arr[n + 1] = arr[n]
                n = n - 1
                arr[n + 1] = s
        return arr

    if y == 0:
        for i in range(1, len(arr)):
            s = arr[i]
            n = i - 1
            while n >= 0 and s < arr[n]:
                arr[n + 1] = arr[n]
                n -= 1
                arr[n + 1] = s
        return arr

for i in range(x):
    p = input().split()
    p[1] = int(p[1])
    arr.append(p)

sort(arr)
for i in range(x):
    print(arr[i][0], arr[i][1])
