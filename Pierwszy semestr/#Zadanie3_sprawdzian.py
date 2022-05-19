word = str(input())
maxi = 0
for i in range(len(word)):
    x = ord(word[i])
    if x > maxi:
        maxi = x
print(maxi)