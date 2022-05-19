a = input()
k = int(input())
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
print(cezar(a, k))