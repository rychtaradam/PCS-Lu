'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def opavaodprahy(rychlost_zvuku):
    '''
    Vypočte čas, jak dlouho bude trvat zvuku překonat vzdálenost mezi Opavou a Prahou.
    '''
    vzdalenost = 249 #km
    cas = (vzdalenost*1000)/rychlost_zvuku
    print(opavaodprahy.__doc__)
    print('Pokud by byla teplota ve vzduchu mezi Opavou a Prahou 20°C, tak by tato vzdálenost trvala rychlosti zvuku překonat za: ', cas, 'sekund.');

def slabsisilnejsi(zemska_gravitace, gravitace_mesice):
    '''
    Vypočte kolikrát je menší gravitace měsíce než gravitace země.
    '''
    vypocet = zemska_gravitace / gravitace_mesice
    print(slabsisilnejsi.__doc__)
    print('Gravitace měsíce je ', vypocet, 'krát menší.')

def prevodnakmh(zgravitace, mgravitace, svetlo, zvuk):
    '''
    Převede všechny konstanty z m/s na km/h.
    '''
    vypocet1 = zgravitace * 3.6 * 3.6
    vypocet2 = mgravitace * 3.6 * 3.6
    vypocet3 = svetlo * 3.6
    vypocet4 = zvuk * 3.6
    print(prevodnakmh.__doc__)
    print('Zemská gravitace v km/h je ', vypocet1, '.')
    print('Měsíční gravitace v km/h je ', vypocet2, '.')
    print('Rychlost světla v km/h je ', vypocet3, '.')
    print('Rychlost zvuku v km/h je ', vypocet4, '.')
