import turtle
import random

turtle.title("Wyścig żółwi")

meta = turtle.Turtle()
meta.penup()
meta.goto(240, 220)
meta.write("Finish Line", font=("Arial", 15, "bold"))
meta.penup()
meta.goto(300, 200)
meta.pendown()
meta.goto(300, -200)
meta.hideturtle()

t1 = turtle.Turtle()
t1.pensize(7)
t1.penup()
t1.goto(-200, 100)
t1.pendown()
t2 = turtle.Turtle()
t2.pensize(7)
t2.penup()
t2.goto(-200, -100)
t2.pendown()

def fd_t1():
    t1.fd(50)
    color = random.choice(["blue","green","cyan"])
    t1.color(color)
turtle.onkey(fd_t1,"w")

def fd_t2():
    t2.fd(50)
    color = random.choice(["yellow","orange","yellow"])
    t2.color(color)
turtle.onkey(fd_t2,"s")
turtle.listen()
while True:
    t1_poz = t1.pos()
    t2_poz = t2.pos()
    if t1_poz[0] >= 300:
        print("The end t1 win!")
        turtle.Screen().bye()
        break
    if t2_poz[0] >= 300:
        print("The end t2 win!")
        turtle.Screen().bye()
        break
    turtle.update()
turtle.mainloop()
turtle.done()