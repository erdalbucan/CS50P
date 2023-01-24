#ideal test dosyasi  'calculator_test.py' dosyasinda yazildi
from calculator import kareal

def main():
    testKareal()

def testKareal():
    #.3 pip install pytest kullanacagiz. info sitesi  docs.pytest.org
    #terminalde 'pytest dosyaadi.py' komutuyla test yapilir.
    assert kareal(2) == 4
    assert kareal(3) == 9
    assert kareal(-2) == 4
    assert kareal(0) == 0
    assert kareal(1) == 1

"""
   #.2 test ederken /assert komutunu da kullanabiliriz
   try:
       assert kareal(2) == 4
   except AssertionError:
       print("2 nnin karesi 4 etmiyor")
   try:
       assert kareal(3) == 9
   except AssertionError:
       print("3 nnin karesi 9 etmiyor")
   try:
       assert kareal(-3) == 9
   except AssertionError:
       print("-3 nnin karesi 9 etmiyor")
   try:
       assert kareal(0) == 0
   except AssertionError:
       print("0 nnin karesi 0 etmiyor")
"""

"""
   #.1 if komutuyla eger  eger eger ler ile test yapma
    if kareal(2) != 4:
        print("2 nin karesi 4 degil")
    elif kareal(3) != 9:
        print("3 karesi 9 degil")
"""

if __name__ == '__main__':
    main()
