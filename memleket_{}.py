#Butun Doslari Dunya vatandasi yapacagiz
dostlar = ["Ali","Orhan","Mirza"]

#dostlar listesinde  for yapip gelen isimleri name ye ekleyecek sekilde listeleme
"""dost_memleketleri = []

for dostmemleketi in dostlar:
    dost_memleketleri.append({"name":dostmemleketi, "house":"citizen of world"})
"""
"""
dost_memleketleri = [{"name":dostmemleketi, "house":"citizen of World"} for dostmemleketi in dostlar]
"""
dost_memleketleri = {dost: "Citizen of World" for dost in dostlar}

#forla doldurdugumuz dost_memleketleri listesini yazdiralim
print(dost_memleketleri) 