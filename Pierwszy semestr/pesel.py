a = input()
b = 0
while (int(b) < int(a)):

    i = input()
    n = 0
    n += (int(i) % 10 * 1)
    i = int(i) / 10
    n += (int(i) % 10 * 3)
    i = int(i) / 10
    n += (int(i) % 10 * 1)
    i = int(i) / 10
    n += (int(i) % 10 * 9)
    i = int(i) / 10
    n += (int(i) % 10 * 7)
    i = int(i) / 10
    n += (int(i) % 10 * 3)
    i = int(i) / 10
    n += (int(i) % 10 * 1)
    i = int(i) / 10
    n += (int(i) % 10 * 9)
    i = int(i) / 10
    n += (int(i) % 10 * 7)
    i = int(i) / 10
    n += (int(i) % 10 * 3)
    i = int(i) / 10
    n += (int(i) % 10 * 1)
    i = int(i) / 10

    if (int(n) == 0):
        print("N")
    elif (int(n) % 10 == 0):
        print("D")
    else:
        print("N")
    b += 1

    a = int(input("Ile peseli chcesz sprawdzić? "))  # sprawdzamy ile peseli chcemy sprawdzić
    for i in range(a):
        b = input("Podaj pesel: ")  # wprowadzamy pesel/e
        if len(b) == 11:  # jeśli pesel ma długość 11, to robimy podany poniżej algorytm
            c = int(b[0])
            d = int(b[1])
            e = int(b[2])
            f = int(b[3])
            g = int(b[4])
            h = int(b[5])
            i = int(b[6])
            j = int(b[7])
            k = int(b[8])
            l = int(b[9])
            m = int(b[10])
            n = int(c * 1) + int(d * 3) + int(e * 7) + int(f * 9) + int(g * 1) + int(h * 3) + int(i * 7) + int(
                j * 9) + int(k * 1) + int(l * 3) + int(m * 1)
            if n % 10 == 0:
                print("D")
            else:
                print("N")