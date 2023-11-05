anEskiSoyad = "kuzucu"

soru1 = input("Lütfen annenizin kızlık soyadının 4. harfini giriniz :").lower()
soru2 = input("lütfen annenizin kızlık soyadının 2. harfini giriniz :").lower()


if soru1 == anEskiSoyad[3] and soru2 == anEskiSoyad[1] :
    print("harfiniz verdiğiniz yerde bulunuyor.")

else :
    print("harfiniz verdiğiniz yerde bulunmuyor.")
    

