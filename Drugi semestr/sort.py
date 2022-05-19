class Person:
    def __init__(self, name, height):
        self.name = name
        self.height=height
arr = []
N = int(input())
for i in range(N):
    nh=input().split()
    person= Person(nh[0], int(nh[1]))
    arr.append(person)
for i in range(1,N):
    key = arr[i]
    j = i - 1
    while j >= 0 and key.height < arr[j].height:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
for e in arr:
    print(e.name, e.height)