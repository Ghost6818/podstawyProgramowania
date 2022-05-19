rok = int(input())
a = rok %19
b = rok %4
c = rok %7
d = (a*19 + 24) %30
e = (2*b + 4*c + 6*d + 5)%7
w = 22 + d + e

if(d == 29 and e ==6) or (d == 28 and e == 6):
    w -= 7
if w > 31:
    w -= 31
print(w)