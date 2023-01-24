# terminalde pip install Black  ile black paketini kuruyoruz
#Style ni duzeltmek istedigimiz dosyamiz icin terminalde.
#black dosyaadi.py komututla dosya style duzeltiliyor.

#web sitesi = https://peps.python.org/pep-0008/

# Ornekler:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

#if kullanimi genelde bu sekilde olur
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

#Liste olusturma genellikle bu sekilde yapilir
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)