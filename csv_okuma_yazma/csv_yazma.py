import csv

isim = input("ismi giriniz...")
memleket = input("Dogum yerini giriniz...")
meslek = input("Meslegini giriniz...")
yas = input("Yasini giriniz...")

with open("csv_yazma.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","d.yeri","yasi","meslegi"])
    writer.writerow({"name":isim, "d.yeri":memleket, "yasi":yas, "meslegi":meslek})
