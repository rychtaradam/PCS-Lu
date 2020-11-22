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

    #Nastaví výšku dané osoby na random hodnotu od 40 do 200cm.
    @staticmethod
    def random_vyska():
        return random.randint(40, 200)

    #Vytvoří novou osobu s nulovými a default hodnotami.
    @classmethod
    def novy(cls):
        return cls("xxx", 0, "xxx", Clovek.defaultVyska, 0, Clovek.defaultBarvaObleceni, "xxx")

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


adam = Clovek("Adam", 18, "M", Clovek.defaultVyska, 92, Clovek.defaultBarvaObleceni, "mu")
alex = Clovek("Saša", 16, "F", Clovek.defaultVyska, 52, Clovek.defaultBarvaObleceni, "jí")
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

osoba = Clovek.novy()
print(osoba)
osoba.vyska = Clovek.random_vyska()
print(osoba)
Clovek.zmena_veku(osoba, 60)
print(osoba)
adam.info()
alex.info()
osoba.info()
