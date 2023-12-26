a=int(input("Birinci Sayı Gir="))
b=int(input("İkinci Sayı Gir="))
c=input("İşlem Seçiniz(+,-,*,/,%,**):")
if c=="+":
    print("sayıların toplamı:",a+b)
elif c=="-":
    print("sayıların çıkartılması",a-b)
elif c=="*":
    print("Sayıların Çarpımı",a*b)
elif c=="/":
    print("Sayıların Bölümü",a/b)
elif c=="%":
    print("Sayıların Yüzdesi",a%b)
elif c=="**":
    print("Üslü Sayılar",a**b)
else:
    print("Doğru Sonuç Giriniz")