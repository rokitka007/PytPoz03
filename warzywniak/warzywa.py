def cena_wyrzywa(warzywo):
    ceny_warzyw = {
        "pomidor": 3.2,
        "ogorek": 3.5,
        "salata": 5,
        "marchew": 2.5
    }
    return ceny_warzyw.get(warzywo)

