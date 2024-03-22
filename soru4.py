#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

#mantık olarak kullanıcnın girdiği sayıyı kendisinden önceki sayılara böleceğiz. 

sayi = int(input("Sayı giriniz:"))
asalmi = 0

for i in range (2,sayi):  # i değeri her döngüde 2 ve kullanıcının girdiği sayı arasındaki değerleri sırayla alacak.  2 yazmanın nedeni: asal sayılar 1 den ve kendisinden başka sayıya bölünmediği için 1'i dışarda bırakmamız lazım.
                           # son değer döngünün dışında oluyor. örn sayı= 9 i=8 olur yani döngü dışı kalır.
    if sayi%i == 0:  #sayi bölü i nin kalanı 0 mı?  %: sayıyı bölüp kalanı alır.
      asalmi += 1 
      break
   

if asalmi == 0:
      print(sayi, "sayısı asaldır.")
else: 
      print(sayi, "sayısı asal değildir.")
      
                   