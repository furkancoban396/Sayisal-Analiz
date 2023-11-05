def faktoriyelAlma(adim):
    faktoriyel = 1
    for i in range(1, adim + 1):
        faktoriyel *= i
    return faktoriyel

def usAlma(sayi, adimsayisi):
    us = 1
    for i in range(0, adimsayisi):
        us *= sayi
    return us

pi = 3.14 / 5
adimsayisi = int(input("Kaç terimli hesaplamak istersiniz?\n\n "))
gercekDeger = 0.80901699437

hesaplananDeger = 0
i = 0
j = 0

for adim in range(1, adimsayisi + 1):
    i = 0
    j = 0
    hesaplananDeger = 0
    while i <= adim:
        if i % 2 == 0:
            hesaplananDeger += usAlma(pi, j) / faktoriyelAlma(j)
        else:
            hesaplananDeger -= usAlma(pi, j) / faktoriyelAlma(j)
        i += 1
        j += 2
    kesmeHatasi = gercekDeger - hesaplananDeger
    print(f"\n{adim}. Mertebedeki;\nHesaplanan Deger: {hesaplananDeger} \nKesme Hatasi: {kesmeHatasi}")
