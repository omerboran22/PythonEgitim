
def asalSayiBul():
  for i in range(2,101):
    kontrol=0
    for a in range(2,i):
      if (i%a==0):
        kontrol=1
    if (kontrol==0):
      print(i,"Asal Sayıdır")

asalSayiBul()