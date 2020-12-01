import random

class Clovek:
    defaultBarvaObleceni = "černé"
    defaultVyska = 175

    def __init__(self, jmeno, vek, pohlavi, vyska, vaha, barvaObleceni, slovo):
        self.jmeno = jmeno
        self.vek = vek
        self.pohlavi = pohlavi
        self.vyska = Clovek.defaultVyska
        self.vaha = vaha
        self.barvaObleceni = Clovek.defaultBarvaObleceni
        self.slovo = slovo

    def __str__(self):
        return f"{ self.jmeno } je { self.pohlavi }, je {self.slovo} { self.vek }, má výšku { self.vyska }cm, váží { self.vaha }kg a má { self.barvaObleceni } oblečení."


class Dospely(Clovek):
    #Nastaví výšku dané osoby na random hodnotu od 40 do 200cm.
    @staticmethod
    def random_vyska():
        return random.randint(40, 200)

    #Vytvoří novou osobu s nulovými a default hodnotami.
    @classmethod
    def novy(cls):
        return cls("xxx", 0, "xxx", Dospely.defaultVyska, 0, Dospely.defaultBarvaObleceni, "xxx")

    #Změní věk osoby.
    def zmena_veku(self, vek):
        self.vek = vek

    #Vypíše pohlaví dané osoby.
    def info(self):
        if self.pohlavi == "M":
            print(f"{self.jmeno} je mužského pohlaví.")
        elif self.pohlavi == "F":
            print(f"{self.jmeno} je ženského pohlaví.")
        else:
            print(f"{self.jmeno} nemá určené pohlaví.")

class StupneCelsia:
    def __init__(self, teplota=0):
        self.teplota = teplota

    def na_Fahrenheit(self):
        return (self.teplota * 1.8) + 32

    @property
    def teplota(self):
        return self._teplota

    @teplota.setter
    def teplota(self, value):
        if value < -273.15:
            raise ValueError("Teplota pod -273 není možná.")
        self._teplota = value


adam = Dospely("Adam", 18, "M", Dospely.defaultVyska, 92, Dospely.defaultBarvaObleceni, "mu")
alex = Dospely("Saša", 16, "F", Dospely.defaultVyska, 52, Dospely.defaultBarvaObleceni, "jí")
alex.vyska = 172
print(adam)
print(alex)

if adam.vek > alex.vek:
    print("Adam je starší než Alex.")

else:
    print("Alex je starší než Adam.")


if alex.vyska == adam.vyska:
    print("Alex je stejně vysoká jako Adam.")

elif alex.vyska > adam.vyska:
    print("Alex je vyšší než Adam")

else:
    print("Adam je vyšší než Alex.")


print(f"Adam je vyšší o {adam.vyska - alex.vyska} cm.")
print(f"Adam a Alex mají dohromady {adam.vek + alex.vek} let.")

osoba = Dospely.novy()
print(osoba)
osoba.vyska = Dospely.random_vyska()
print(osoba)
Dospely.zmena_veku(osoba, 60)
print(osoba)
adam.info()
alex.info()
osoba.info()

lidske_telo = StupneCelsia(36)
print(lidske_telo.teplota)
print(lidske_telo.na_Fahrenheit())
test_properties = StupneCelsia(-300)
