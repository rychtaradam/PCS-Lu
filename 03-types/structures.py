veta = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."

def charFrequency(veta):
    frekvence = {}
    for pismena in veta:
        keys = frekvence.keys()
        if pismena in keys:
            frekvence[pismena] += 1
        else:
            frekvence[pismena] = 1
    return frekvence


print('Věta: ' + veta)
print('Četnost výskytu písmen:')
print('-----------------------')
print(charFrequency(veta))