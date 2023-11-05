x = 3.14159265359 / 5

n = int(input("Kaç terimli hesaplamak istersiniz? "))

gercek_deger = 0.8090169943749475 

ilk_terim = 1.0
yaklasik_deger = 1.0

for i in range(1, n):
    yaklasik_deger *= (-1) * x ** (2 * i) / (2 * i * (2 * i - 1))
    ilk_terim += yaklasik_deger
    
kesme_hatasi = abs(gercek_deger - ilk_terim)

print("Yaklaşık Değer:", ilk_terim)
print("Gerçek Değer:", gercek_deger)
print("Kesme Hatası:", kesme_hatasi)
