from warzywniak.owoce import ceny_owocow
from warzywniak.warzywa import cena_wyrzywa


def doliczPodatek(cena):
    return round(cena + cena * 0.23, 2)


if __name__ == '__main__':
    warzywa = ["pomidor", "ogorek", "salata", "marchew"]
    owoce = ["banan", "jablko", "ananas", "brzoskwinia"]
    cena_w, cena_o = 0, 0
    for el in warzywa:
        cena_w += doliczPodatek(cena_wyrzywa(el))
    for el in owoce:
        print(doliczPodatek(ceny_owocow(el)))
        cena_o += doliczPodatek(ceny_owocow(el))

    print("Cena warzyw: " + str(cena_w))
    print("Cena owocow: " + str(round(cena_o, 2)))
    print("Cena calosci: " + str(cena_w + cena_o))


