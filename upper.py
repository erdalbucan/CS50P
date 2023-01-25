#hedefimiz "This is CS50" stingini butununu buyuk harfler yazdirmak

#Ana fonksyo tanimliyoruz
def main():
    yell("This is CS50")

#yell fonksyonnu tanimliyoruz
def yell(*words):
    #liste olusturup dongu ile listenin icine buyuk harfleri ekliyoruz
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()