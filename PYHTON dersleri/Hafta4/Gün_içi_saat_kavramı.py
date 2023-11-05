saat = int(input("Lütfen saat giriniz :"))


if  0 < saat <7:
    print("İyi geceler")

elif 7<= saat <= 10:
    print("Günaydın")

elif 11<= saat <= 17:
    print("İyi günler")

elif 18<= saat <= 21:
    print("İyi akşamlar")

elif 22<= saat <= 24:
    print("İyi geceler")

else :
    print("Lütfen 24 saatlik sayı sistemine göre saat girin!")
