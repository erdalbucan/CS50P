# test yazilimi, terminalde 'pytest dosyaAdi.py' komutuyla test edilir
# test edilecek yazilimi cagiriyoruz.
from calculator import kareal

def test_pozitif():
    assert kareal(2) == 4
    assert kareal(3) == 9

def test_negatif():
    assert kareal(-2) == 4
    assert kareal(-3) == 9

def test_zero():
    assert kareal(0) == 0

def test_one():
    assert kareal(1) == 1


