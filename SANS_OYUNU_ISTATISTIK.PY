import random
import json

#Sayisal Lotoda toplamda 60 top var
top_sayisi = list(range(1,61))

#Satilan bilet fiyatini giriniz
Bilet_fiyati = 6 #int(input("bilet fiyatini giriniz"))

#Program acilisinda gelen Bilgilendirme ekran yazisi
print(f"""
PROGRAMIN HEDEFI CekilisE belirlediginiz kadar bilet alirsaniz ne kadar ikramiye kazanilabilecegi;\n
bilet satin alma masraflari ve ikramiye gelirleri simulasyonunu cikarmaktir...
\n\n30.01.2023 tarihli Süper Loto İkramiye Tutarı baz alinmistir!!!\n\n
6li Buyuk ikramie 47.624.485 YTL\n
5li Ikramiye 36.915 YTL\n
4lu ikramiye 691 YTL\n
3lu ikramiye 36 YTL\n
2li ikramiye 4 YTL\n
Bilet Fiyati 6 YTL\n\n"""
)

#cekilis basina gunluk alinan bilet sayisi
alinan_bilet_sayisi = int(input("Kac Adet Bilet Almak Istiyorsunuz ?  "))

#ocak2023  te 13 oyun oynanmis, burdan yola cikarak yilda oynanan oyun sayisi
yilda_oyun_sayisi = 12*13
cekilis_sayisi = 1

#ikramiyelerin degerleri
tutturulan_sayi_6 = 47000000 #int(input("6 tutana verilecek ikramiy1 giriniz"))
tutturulan_sayi_5 = 36700 #int(input("5 tutana verilecek ikramiy1 giriniz"))
tutturulan_sayi_4 = 690 #int(input("4 tutana verilecek ikramiy1 giriniz"))
tutturulan_sayi_3 = 37 #int(input("3 tutana verilecek ikramiy1 giriniz"))
tutturulan_sayi_2 = 4 #int(input("2 tutana verilecek ikramiy1 giriniz"))

Toplam_harcanan_fiyat = 0 #biletler icin toplam odenen
Toplam_kazanilan_ikramiye =0 #kazanilan toplam ikramiye

#lotoda 3 4 5 6 bilene gore farkli ikramiyeler olusturuyoruz
kazanilan_loto = {
    "6 tuttu ":0,
    "5 tuttu ":0,
    "4 tuttu ":0,
    "3 tuttu ":0,
    "2 tuttu ":0,
}

# satir 89 da aciklamasi yapilan biletleri elimizdeki bilet ile kazanan bileti karsilastirma fonksyonu
def bilet_karsilastir(Elimizdeki_bilet, kazananNumaralar):
    kazanilan_ikramiye = 0

    #Elimizdeki_bilet.intersection(kazananNumaralar) ile kazanan numaralar ile elimizdeki numaralari kesistiriyoruz
    #len() ile kac sayi tutmus 2 tutturdun 3 tutturdun 6 tutturdun vs
    tutan_sayi = len(Elimizdeki_bilet.intersection(kazananNumaralar))
    if tutan_sayi == 6:
        kazanilan_ikramiye = tutturulan_sayi_6
        kazanilan_loto['6 tuttu '] += 1
    
    elif tutan_sayi == 5:
        kazanilan_ikramiye = tutturulan_sayi_5
        kazanilan_loto["5 tuttu "] += 1

    elif tutan_sayi == 4:
        kazanilan_ikramiye = tutturulan_sayi_4
        kazanilan_loto["4 tuttu "] += 1

    elif tutan_sayi == 3:
        kazanilan_ikramiye = tutturulan_sayi_3
        kazanilan_loto["3 tuttu "] += 1

    elif tutan_sayi == 2:
        kazanilan_ikramiye = tutturulan_sayi_2
        kazanilan_loto["2 tuttu "] += 1
    
    return kazanilan_ikramiye


for numara in range(cekilis_sayisi):
    # 6 adet rasgele benzersiz(sample)numara cekiyoruz, set()ile listeyi dictinery ceviriyorum
    kazananNumaralar = set(random.sample(top_sayisi, k=6)) 

    for bilet in range(alinan_bilet_sayisi):
        Toplam_harcanan_fiyat += Bilet_fiyati
        Elimizdeki_bilet = set(random.sample(top_sayisi, k=6))

        #elimizdeki bileti kazanan biletle karsilastirmak icin fonsyon yazmaliyim, 51 satirda yeni fonsyon olusturuyorum
        kazanilan_ikramiye = bilet_karsilastir(Elimizdeki_bilet, kazananNumaralar)
        Toplam_kazanilan_ikramiye += kazanilan_ikramiye


print(f'\n\nBiletlere Harcanan Toplam Fiyat   {Toplam_harcanan_fiyat} Ytl\n')
print(f'Kazanilan Toplam Ikramiye   {Toplam_kazanilan_ikramiye} Ytl\n\n')
print(json.dumps(kazanilan_loto, indent=2))
