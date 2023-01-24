arkadaslar = []

with open("names.csv") as file:
    for satir in file:
        isim, memleket,yasam = satir.rstrip().split(",")
        arkadas = {"isim":isim, "memleket":memleket,"yasadigiYer":yasam}
        arkadaslar.append(arkadas)

"""
        # arkadas = {"isim":isim, "memleket":memleket} komutuyla uc satir tek satira iner
        arkadas = {}
        arkadas["isim"] = isim
        arkadas["memleket"] = memleket
"""
#key=lambda arkadas:arkadas['isim'] komutuyla sorted komutunun calismasina imkan veriyoruz
for arkadasim in sorted(arkadaslar,key=lambda arkadas:arkadas['isim']):
    print(f"{arkadasim['isim']} beyin memleketi {arkadasim['memleket']}")

""" # asagidaki 4 satir yerine tek satirda for dongusunde key=lambda arkadas: arkadas[ísim'] kodu
def get_isim(arkadas):
    return arkadas['isim']

def get_memleket(arkadas):
    return arkadas['memleket']

for arkadasim in sorted(arkadaslar, key = get_isim, reverse=True):
    print(f"{arkadasim['isim']} Beyin memleketi {arkadasim['memleket']} dir")
"""

"""
#isimler uzerinden alfabetik siralama icin once liste olusturup ekliyoruz
ogrenciler = []

with open("names.csv") as file:
    for satir in file:
        isim,memleket = satir.rstrip().split(",")
        ogrenciler.append(f"{isim} Beyin Memleketi {memleket} dir")

for ogrenci in sorted(ogrenciler):
    print(ogrenci)
"""

"""
#1 name.csv dosyasini okuyup virgulle ayrilmis -Ali,kayseri- vb. degerleri kullanmak
with open("names.csv") as file:
    for satir in file:
        isim,memleket = satir.rstrip().split(",")
        print(f"{isim} beyin memleketi {memleket} dir")
"""

"""
        row = satir.rstrip().split(",") #.split(",") komutuyla , ile ayrilan kelimeleri ayri ayri aliyoruz
        print(f"{row[0]} beyin yasadigi yer {row[1]} dir") # virgulle indexten okunur x[0],x[1]
 """

