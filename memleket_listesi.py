#Hedefimiz Listemizdeki Sumgayitli dostlarimizi yazdirmak 
dostlar = [
    {"name":"Ali Demir", "house":"Kayseri"},
    {"name":"Orhan Malkocoglu", "house":"Rize"},
    {"name":"Mirze Shukurov", "house":"Sumgayid"},
    {"name":"Ersin Mlm", "house":"Helsinki"},
    {"name":"Zaur Baltaci", "house":"Sumgayid"},
]

"""
#Formule dikkat = name adinda dostlar listesinde dongu yap ve donen sumgayit ise  Sumgayih listesi olustur 
Sumgayid = [
    dost["name"] for dost in dostlar if dost["house"] == "Sumgayid"
]
# oncelikle dongu ile olusturdugumuz Sumgayid listesini yazdiriyorum
print(Sumgayid)

#Sumgayitli dost isimlerini ayri ayri yazdirmak istiyorum.
for dost_isimleri in sorted(Sumgayid):
    print(dost_isimleri)
"""

#housesi Sumgayid olanlari gonder fonksyonu
def is_Memleket(m):
    return m["house"] == "Sumgayid"

#is memleket fon. dostlara uygulayan filter ile memleketler klas filtresi olusturuyoruz
memleketler = filter(is_Memleket, dostlar)

for dost_memleketi in memleketler:
    print(dost_memleketi["name"])
