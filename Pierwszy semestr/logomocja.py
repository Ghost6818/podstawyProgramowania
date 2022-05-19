import turtle
#Napisz program, który narysuje 3 kwadraty o boku 100 obok siebie, korzystając z funkcji z zadania 3.
#Napisz program, który narysuje x kwadratów o boku 100 obok siebie, korzystając z funkcji z zadania 3. Liczbę x wczytaj
#od użytkownika.
#Napisz program, który narysuje "domek" korzystając z funkcji rysujących kwadrat oraz trójkąt.
#Napisz program, który narysuje spiralę jak na rysunku spiral.png.
#Napisz program, który narysuje rysunek circle.png za pomocą metody circle.

x = int(input())
t = turtle.Turtle()
def funkcja(a):
    for i in range(4):
        t.fd(a)
        t.rt(90)

for i in range(x):
    funkcja(100)
    t.up()
    t.fd(140)
    t.down()


turtle.done()