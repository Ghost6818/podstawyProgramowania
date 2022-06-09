lista = [4, 3, 8, 1, 2, 9]


def SortowanieWstawianie(lista):
    for i in range(1, len(lista)):
        if lista[0] > lista[i+1]:
            lista[0], lista[i + 1] = lista[i+1], lista[0]
        if lista[0] < lista[i+1]:
            lista[0], lista[i+1] = lista[0], lista[i+1]
        print(lista)

SortowanieWstawianie([4, 3, 8, 1, 2, 9])