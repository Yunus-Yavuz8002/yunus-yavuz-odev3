sayilar = [3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.
#x=0
#for x in sayilar:
#    print(x)

# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?
#x=0
#while(x<=6):
#    if(sayilar[x]%3==0):
#        print(sayilar[x])
    
#    x+=1
# 3- "sayilar" listesinde tüm sayıların toplamı nedir?
#sonuc=sum(sayilar)
#print(sonuc)


urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (index ve find komutlarından faydalanınız.)
#iphonelar= [urun for urun in urunler if urun.find("iphone") != -1]
#print(iphonelar)


# 5- "urunler" listesinde kaç adet samsung ürünü vardır? (find metodu)
samsunglar= [urun for urun in urunler if urun.find("iphone") != -1]
print(samsunglar)
