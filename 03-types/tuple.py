'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
V Pythonu jsou n-tice psány s kulatými závorkami.
'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# Chcete-li vytvořit n-tici pouze s jednou položkou, přidáte za položku čárku, pokud Python nerozpozná proměnnou jako n-tici.
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot 
# Rozsah indexů můžete určit zadáním, kde začít a kde rozsah ukončit.
# Při zadávání rozsahu bude návratovou hodnotou nová n-tice se zadanými položkami.
print(f'chars[2:5]: {chars[2:5]}')

# Negativní indexování znamená, že začíná od konce, -1 označuje poslední položku, -2 označuje druhou poslední položku atd.
# Určete záporné indexy, pokud chcete zahájit vyhledávání od konce n-tice:
# Tento příklad vrací položky z indexu -4 (zahrnuto) do indexu -1 (vyloučeno)
print(f'chars[-4:-1]: {chars[-4:-1]}')

# Chcete-li zjistit, kolik položek má n-tice, použijte metodu len ():
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
