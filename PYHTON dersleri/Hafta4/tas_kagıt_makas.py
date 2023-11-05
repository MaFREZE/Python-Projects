oyuncu1 = input(" oyuncu1 bir madde seçin : ")

oyuncu2 = input(" oyuncu2 bir madde seçin : ")


if (oyuncu1 == "tas" and oyuncu2 == "tas") or (oyuncu1 =="kagıt" and oyuncu2 == " kagıt") or (oyuncu1=="makas" and oyuncu2=="makas") :
    print("berabere")

elif (oyuncu1 == "tas" and oyuncu2 == "makas") or (oyuncu1 =="kagıt" and oyuncu2 == "tas") or (oyuncu1 =="makas" and oyuncu2 == "kagıt") :
    print("oyuncu1 kazandı")

elif (oyuncu1 =="tas" and oyuncu2 == "kagıt") or (oyuncu1 =="kagıt" and oyuncu2 =="makas") or (oyuncu1 =="makas" and oyuncu2 =="tas") :
    print("oyuncu2 kazandı")

else :
    print(" lütfen tas, kagıt ya da makas giriniz")
