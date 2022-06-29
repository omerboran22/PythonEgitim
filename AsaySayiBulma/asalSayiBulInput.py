def asalSayiBul():
 
 try:
    limit =int(input("asal Sayı Sınırını Gir Lütfen : "))
    for i in range(2,limit):
      kontrol=0
    for a in range(2,i):
      if (i%a==0):
        kontrol=1
    if (kontrol==0):
      print(i,"Asal Sayıdır")
 except ValueError:
   print("lütfen Sayı Giriniz")
   asalSayiBul()
 

asalSayiBul()