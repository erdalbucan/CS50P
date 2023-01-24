name = input("What is your name?")

#with komutuyla names.txt adli dosyayi open yapip as komutuyla adina file diyoruz
#dosya adini verdikten sonra "a" komutuyla dosya eknenebilen formatta aciliyor "w" durumunda ustune yazilacakti.
with open("../names.txt", "a") as file:
    file.write(f"{name}\n")#file.write ile yazdiriyoruz ve \n komutuyla bir alt satira ekleme yapiyoruz

"""
#txt dosyasi aciyoruz
file = open("names.txt","a") #w=ustune yaz, a=dosyaya ekle
file.write(f"{name}\n")
file.close
"""