 ogrenci = input("Lütfen öğrenci numaranızı giriniz : ")

if len(ogrenci) == 10 and ogrenci[2] == "-" and ogrenci[6] == "-":
    yil = ogrenci[:2]
    bölüm = int(ogrenci[3:6])
    tarih = int(ogrenci[-3:])

    print(f"20{yil} yılında {bölüm} numaralı bölüme kaydolan {tarih}. öğrencisiniz.")

   
