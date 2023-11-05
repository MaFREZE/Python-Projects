sayi1 = int( input("Birinci sayıyı giriniz : "))

operatör =  input(" Operatör seçiniz: '*' veya '/' veya '-' veya'+'. ")

sayi2 = int( input("İkinci sayıyı giriniz : " ))



if operatör == "+":
    print(sayi1 + sayi2)

elif operatör == "-":
    print(sayi1 - sayi2)

elif operatör == "*":
    print(sayi1 * sayi2)

elif operatör == "/":
    if sayi2 != 0:
       print(sayi1 /sayi2)
    else:
        print("Sıfıra bölünemez")
else:
    print("Lütfen geçerli bir veri giriniz")
    
 
