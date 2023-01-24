

# bos names listesi acip kullaniciya doldurtmak
names = []

#listeye eklemekistedigimis isim sayisini range(x) komutuyla belirleyebiliriz
for _ in range(3):
    """
    name = input("What is your name?")
    names.append(name)
    """
    #names listesine inputu eklemek icin .append komutunu kullaniyoruz
    names.append(input("What is your Name?"))

#harf sirasina gore listeyi yazdirmak icin sorted(x) komutunun kullanabiliriz.
for name in sorted(names):
    print(f"hello,{name}")
