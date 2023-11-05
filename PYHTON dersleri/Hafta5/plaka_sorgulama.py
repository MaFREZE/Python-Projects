plaka= input("plaka giriniz >>>> ")

if len(plaka) <=9 and plaka.isalnum() == True and plaka.isnumeric() == False and plaka.isalpha() == False:
    if plaka[:2].isnumeric() == True and int(plaka[:2])<= 81  :
        if plaka[-2:].isnumeric() == True and int(plaka[-2:])<=99 or plaka[-3:].isnumeric()== True and int(plaka[-3:])<= 999 :
            if plaka[2].isalpha() == True or plaka[2:4].isalpha() == True or plaka[2:5].isalpha() == True:
                if plaka[2:3].isalpha()== "T":
                    print("Bu plaka TAKSİ plakasıdır. ")
                if plaka[2:3].isalpha()== "M":
                    print("Bu plaka MİNİBÜS plakasıdır. ")
                if plaka[2:3].isalpha()== "S":
                    print("Bu plaka SERVİS plakasıdır. ")
                





else :
    print("plaka hatalı karakter sayısı!")





