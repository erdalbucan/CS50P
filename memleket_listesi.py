#Hedefimiz Listemizdeki Sumgayitli dostlarimizi yazdirmak 
dostlar = [
    {"name":"Ali Demir", "house":"Kayseri"},
    {"name":"Orhan Malkocoglu", "house":"Rize"},
    {"name":"Mirze Shukurov", "house":"Sumgayid"},
    {"name":"Ersin Mlm", "house":"Helsinki"},
    {"name":"Zaur Baltaci", "house":"Sumgayid"},
]

#Formule dikkat = name adinda dostlar listesinde dongu yap ve donen sumgayit ise  Sumgayih listesi olustur 
Sumgayid = [
    dost["name"] for dost in dostlar if dost["house"] == "Sumgayid"
]
# oncelikle dongu ile olusturdugumuz Sumgayid listesini yazdiriyorum
print(Sumgayid)

#Sumgayitli dost isimlerini ayri ayri yazdirmak istiyorum.
for dost_isimleri in sorted(Sumgayid):
    print(dost_isimleri)
