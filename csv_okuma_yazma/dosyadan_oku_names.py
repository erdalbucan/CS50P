names =[]

with open("../names.txt") as file:
    for satir in file:
        names.append(satir.rstrip()) #

for name in sorted(names):
#for name in sorted(names, reverse=True): reverse=True komutuyla liste tersine cevrilir
    print(f"hello,{name}")

"""
#open ile dosya adini "r" komutuyla okuma modunda aciyoruz ve as komutuyla fileye mapliyoruz
with open("names.txt", "r") as file :
#with open("names.txt", "r") as storted(file): filedeki satirlari harf sirasina gore getirir
    for satir in file: #file deki satir lari dondur.
        print("Hello, ",satir.rstrip())
"""

#.1 asagidaki cadlamaa da dogru fakat pythonic codlama usteki
"""
with open("names.txt", "r") as file :
    satirlar = file.readlines()#file deki satirlari oku

#satirlari for dongusuyle alalim
for satir in satirlar:
    #print(f"Hello, {satir}")
    print("Hello,", satir.rstrip()) #.rstrip() satir basluklarini vs temizler ve satiri direk yazdirir.
    #print(f"Hello, {satir}", end="")
"""

