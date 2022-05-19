from turtle import *

def koch(length,level):
    if level == 0:
        fd(length)
        return
    else:
        length = length/3
        koch(length,level - 1)
        lt(60)
        koch(length,level - 1)
        rt(120)
        koch(length,level - 1)
        lt(60)
        koch(length,level - 1)
def p(length,level):
    penup();backward(180);pendown()
    for i in range(3):
        koch(length,level)
        rt(120)
tracer(0); p(200,3); update()
mainloop()
