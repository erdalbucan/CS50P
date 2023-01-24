from hello import hello

def test_default():
    assert hello() == "Hello, world"

def test_arqument_1():
    assert hello("Erdal") == "Hello, Erdal"

#for dongusuyle test yapmak icin;
def arqument_2():
    for name in ["Ali","Mirza","Orhan","Kenan","Adem","Cemal","Kemal",]:
        assert hello(name) == f"Hello, {name}"

def test_numeric():
    assert hello("100") == "Hello, 100"

#farkli bir klasorden test yapabilmek icin test dosyasinin bulundugu
                #klasore '__init__.py' adli bos dosya olusturuyoruz