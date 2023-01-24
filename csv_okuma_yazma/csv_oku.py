import csv

arkadaslar = []

with open("csv_file.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        arkadaslar.append({
            "name":row["isim"],
            "yas":row["yas"],
            "memleket":row["memleket"],
            "yasamYeri":row["yasamYeri"],
            "is":row["meslek"]
        })

for arkadasim in sorted(arkadaslar, key= lambda arkadasim: arkadasim['name']):
    print(f"{arkadasim['name']} Beyin meslegi {arkadasim['is']} memleketi {arkadasim['memleket']}")


