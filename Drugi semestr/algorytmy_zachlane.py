n = [500, 200, 100, 50, 20, 10, 5, 2, 1]
r = int(input())

w = []
i = 0
while r > 0:
    if r >= n[i]:
        w.append(n[i])
        r -= n[i]
    else:
        i += 1
print(w)