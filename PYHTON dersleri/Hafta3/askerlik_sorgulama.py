
s1=input("Cinsiyetinizi giriniz : ")

if s1=="e":
    print("Askerlik için cinsiyetiniz uyumlu. ")
    yas = int(input("yaşınızı giriniz : "))
    if  yas > 17 and yas <= 64:
        print("Yaşınız askerliğe uygundur.")
    else :
        print("Yaşınız askerliğe uygun değildir !")
        

elif s1=="k":
    print("Askerlik için cinsiyetiniz uyumlu değil !")



