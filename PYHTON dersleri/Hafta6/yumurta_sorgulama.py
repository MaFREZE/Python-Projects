egg_num = input("Lütfen yumurta üstündeki kodu giriniz :")

if len(egg_num) == 13 and egg_num.isalnum() == True and egg_num.isnumeric() == False and egg_num.isalpha() == False: #1TR24315654
    uretim_kodu = egg_num[0]
    ulke_kodu = egg_num[1:3]
    sehir_kodu = egg_num[3:5]
    isletme_kodu = (egg_num[5:])
    if egg_num[0].isnumeric() == True and int(egg_num[0])<=2 :
        if uretim_kodu == "0":
            uretim_kodu = "ORGANİK"
        elif uretim_kodu == "1":
            uretim_kodu = "SERBEST GEZEN"
        elif uretim_kodu == "1":
            uretim_kodu = " KÜMES"
    if ulke_kodu.isalpha() == True:
        if ulke_kodu == "TR":
            ulke_kodu = "TÜRKİYE"
        elif ulke_kodu == "FR":
            ulke_kodu = "FRANSA"
    if sehir_kodu.isnumeric() == True:
        if sehir_kodu == "33":
            sehir_kodu = "MERSİN"
        elif sehir_kodu == "34":
            sehir_kodu = "İSTANBUL"
        elif sehir_kodu == "35":
            sehir_kodu = "İZMİR"

    if isletme_kodu.isnumeric() == True:
        
     print(f"bu {ulke_kodu} ülkesinin {sehir_kodu} ilinde {isletme_kodu} işletmesinde {uretim_kodu} türünde bir yumurtadır.")
