import math
def m(sr, l, r):
    i_l = i_r = i = 0
    while i_l < len(l) and i_r < len(r):
        if float(l[i_l][2]) >= float(r[i_r][2]):
            sr[i] = l[i_l]
            i_l += 1
        else:
            sr[i] = r[i_r]
            i_r += 1
        i += 1
    while i_l < len(l):
        sr[i] = l[i_l]
        i += 1
        i_l += 1
    while i_r < len(r):
        sr[i] = r[i_r]
        i += 1
        i_r += 1

def merge(sr):
    if len(sr) > 1:
        s = len(sr)//2
        left = sr[:s]
        right = sr[s:]
        merge(left)
        merge(right)
        m(sr,left,right)

l = int(input())
for i in range(l):
    sr = []
    dane = input()
    while dane != '-':
        arr = dane.split()
        sr.append(arr)
        dane = input()
    if len(sr) > 1:
        merge(sr)
        x = math.ceil(len(sr) * 0.1)
        for n in range(x):
            print(sr[n][0],sr[n][1])
        print('-')
    else:
        pass

#miłego dnia :)