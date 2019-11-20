from pakiet1.ceny import sredniaCena

c = "cos"

def podaj_zwierze(wielkosc):
    zwierze = ""
    if wielkosc == "male":
        zwierze = "chomik"
    elif wielkosc == "srednie":
        zwierze = "kot"
    elif wielkosc == "duze":
        zwierze = "kon"
    else:
        print("Nie mamy innej wielkosci zwierzat")
    return zwierze


if __name__ == '__main__':

    print(podaj_zwierze("moje"))
    print(podaj_zwierze("male"))
    print(podaj_zwierze("srednie"))
    print(podaj_zwierze("duze"))

    wielkosc = ["male", "srednie", "duze"]
    cena = 0
    for wl in wielkosc:
        cena += sredniaCena(podaj_zwierze(wl))
    print("Za zwierzeta musisz zaplacic " + str(cena))