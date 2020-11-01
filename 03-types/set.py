'''
 Set je množina jedinečných hodnot
 Sada je kolekce, která je neuspořádaná a neindexovaná.
 V Pythonu jsou sady psány složenými závorkami.
'''
my_set = {2, 3, 9, 7}
print('Množina my_set: ', my_set)
print('Typ my_set: ', type(my_set))

# Vytvoření množiny ze seznamu hodnot (list)
numbers = [1, 4, 1, 5, 3, 3, 1, 2, 8, 2]
print(f'Proměnná numbers - seznam (list): {numbers}')
set_numbers = set(numbers)
print(f'Proměnná set_numbers - množina (set): {set_numbers}')

# Vytvoření množiny jedinečných znaků z řetězce
chars = sorted(list('Hello world'))
set_chars = set(chars)
print(f'Uspořádaná množina (set) jedinečných hodnot: {set_chars}')

# Jakmile je sada vytvořena, nemůžete měnit její položky, ale můžete přidávat nové položky.
# Chcete-li přidat jednu položku do sady, použijte metodu add ().
set_chars.add('V')

# Chcete-li do sady přidat více než jednu položku, použijte metodu update ().
set_chars.update('X', 'Y', 'Z')

# Chcete-li odebrat položku v sadě, použijte metodu remove () nebo discard ().
set_chars.remove('H')
print(f'Proměnná set_chars: {set_chars}')

# Metoda clear () vyprázdní sadu
set_chars.clear()

# Klíčové slovo del sadu zcela odstraní:
del set_chars

# Přístup k hodnotám množiny
# K položkám v sadě nemůžete přistupovat odkazem na index, protože sady jsou neuspořádané, položky nemají index.
# my_set[1]

# Ale můžete procházet sady položek pomocí smyčky for, nebo se zeptat, jestli je zadaná hodnota v sadě, pomocí klíčového slova in.
for x in my_set:
  print(x)

'''
Množinové operace
'''
# Sjednocení množin
print(f'set_numbers | my_set: {set_numbers | my_set}')
print(f'set_numbers.union(my_set): {set_numbers.union(my_set)}')
# Průnik množin
print(f'set_numbers & my_set: {set_numbers & my_set}')
print(f'set_numbers.intersection(my_set): {set_numbers.intersection(my_set)}')
# Rozdíl množin
print(f'set_numbers - my_set: {set_numbers - my_set}')
print(f'set_numbers.difference(my_set): {set_numbers.difference(my_set)}')
# Doplněk množin
print(f'set_numbers ^ my_set: {set_numbers ^ my_set}')
print(f'set_numbers.symmetric_difference(my_set): {set_numbers.symmetric_difference(my_set)}')
# Zjištění zda množina obsahuje hodnotu
print(f'1 in set_numbers: {1 in set_numbers}')
