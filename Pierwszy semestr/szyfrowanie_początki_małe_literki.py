def szyfruj(text, k):
    s_text = ''
    for n in text:
        a = ord(n)
        b = a + k
        if b > ord('z'):
            b = ord('a') + b - ord('z') -1
        c = chr(b)
        s_text += c
    return s_text
bum = szyfruj ('z', 1)
print(bum)