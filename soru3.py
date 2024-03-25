#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
# gcd komutu ve math metodu

import math 
sayi1=int(input("Birinci Sayıyı Giriniz: "))
sayi2=int(input("İkinci Sayıyı Giriniz: "))

ebob=math.gcd(sayi1, sayi2)
ekok=(sayi1*sayi2)// ebob

print("EBOB:", ebob)
print("EKOK:", ekok)