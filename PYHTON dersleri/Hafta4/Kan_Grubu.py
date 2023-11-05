kisi =input("Kan grubunuzu giriniz : ")

if kisi == "Arh+":
    print("Verebildiği: A+,AB+. Alabildiği: 0+-, A+-.")

elif kisi == "Arh-":
    print("Verebilidiği: A+-, AB+-. Alabildiği: 0-,0-.")

elif kisi == "Brh+":
    print("Verebildiği: B+,AB+. Alabilidği: 0+-, B+-.")

elif kisi == "Brh-":
    print("Verebildiği: B+-,AB+-. Alabildiği: 0-, B+.")

elif kisi =="ABrh+":
    print("Verebildiği: AB+. Alabilidiiği: A+-,B+-,0+-,AB+-.")

elif kisi =="ABrh-":
    print("Verebildiği: AB+-. Alabildiği: A-,B-,AB-,0-.")

elif kisi == "0rh+":
    print("Verebildiği: A+,B+,0+,AB+. Alabildiği : 0+-.")

elif kisi == "0rh-":
    print("Verebildiği: A+-,B+-,AB+-,0+-. Alabildiği : 0-.")

else:
    print("Lütfen düzgünce kan gurubunuzu giriniz!")
