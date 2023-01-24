import sys

"""
try:
    print ("Hello, my name is", sys.argv[1])
    print ("Hello, my name is", sys.argv[0]) # index 0 olunda dosya adini getirir
    # sys.argv[1] kullandiginda, terminalde dosyayi calistirirken yanina yazdigin ismi programa getirir
except IndexError:
    print("Too Few Arguments")
"""
"""
if len(sys.argv) < 2:
     print ("Too Few Arguments(cok az veri)")
elif len(sys.argv) > 2:
    print("Too many Arguments(cok fazla veri)")
else:
    print("hello, my name is",sys.argv[1])
    
"""
"""
if len(sys.argv) < 2 :
    sys.exit("Too Few arguments")
elif len(sys.argv) > 2 :
    sys.exit("Too Many Arguments")

print("Hello, my name is",sys.argv[1])
"""
if len(sys.argv) < 2 :
    sys.exit("Too Few arguments")

for name in sys.argv[1:]: #for name in sys.argv: yaptigimizda 0.indexide aliyor ve dosya adini da yazdiriyor. 1. indexten sonrasini loop ediyoruz
    print("hello my name is",name)




