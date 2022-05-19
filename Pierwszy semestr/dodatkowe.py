def funkcja(lista):
    minimum = lista [0]
    maksimum = lista [0]
    for i in range(0, len(lista) - 1,2):
        if lista[i] > lista[i +i]:
            if lista[i] > maksimum:
                maksimum = lista[i]
            if lista[i+1] < minimum:
                minimum = lista[i + 1]
        else:
                if lista[i + 1] > maksimum:
                    maksimum = lista[i + 1]
                if lista[i] < minimum:
                    minimum = lista[i]
    if not len(lista) % 2 == 0:
        if lista[-1] > maksimum:
            maksimum = lista[-1]
        elif lista[-1] < minimum:
            minimum = lista[-1]
    return minimum, maksimum