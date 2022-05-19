tekst=input()
KLUCZ=int(input())
def deszyfruj(tekst, KLUCZ):
    odszyfrowany = ""
    KLUCZM = KLUCZ % 26
    for znak in tekst:
        if (ord(znak) - KLUCZM < ord('a')):
            odszyfrowany += chr(ord(znak) - KLUCZM + 26)
        else:
            odszyfrowany += chr(ord(znak) - KLUCZM)
    return odszyfrowany
result = deszyfruj(tekst, KLUCZ)


def cezar(a, k):
    key_mood = k% 26
    napis = ''
    for i in a:
        if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            litera = ord(i) + key_mood
            napis += chr(litera)
        else:
            a = ord('a') + (ord(i) + key_mood - ord('z'))
        if (ord(i) >= ord('A') and ord(i) <= ord('Z')):
            litera = ord(i) + key_mood
            napis += chr(litera)
        else:
            a = ord('a') + (ord(i) + key_mood - ord('z'))
    return  napis
result=cezar(tekst, KLUCZ)
print(tekst)
print(result)
print(deszyfruj(result, KLUCZ))