import math
from pakiet1.ceny import b
import os

def poczatki_napisy():
    print("Jakis teskst")
    a = 2
    print(id(a))
    print(id(2))
    print(id(a) == id(2))
    # ctrl + lewy przycisk myszy - przejdz do deklaracji
    print(b)
    # Funkcja getcwd bibliotek os zwraca nam miejsce w katalogu ścieżek, w którym aktualnie się znajdujemy (z którego wywołujemy program)
    print(os.getcwd())
    print(os.path.exists(os.getcwd()))
    # Stringi
    # Kazdy znak w programu Char
    napis1 = "moj pierwszy"
    napis2 = 'moj drugi'
    napis4 = "moj pierwszy 'napis'\""
    napis3 = "moj pierwszy 'napis' "
    print(napis1 + " " + napis2)
    print(napis1.find("drugi"))
    print(len(napis1))

def pierwiastek(liczba):
    return math.sqrt(liczba)

if __name__ == '__main__':

    #Funkcja realizujaca nauke napisow
    poczatki_napisy()
    poczatki_napisy()

    #Funkcja realizujaca pierwiastek z liczby
    print(pierwiastek(25))


    # integer, long - liczba całkowita
    # double, float - zmiennoprzecinkowe
    # +, -, * mnozenie, / dzielenie % reszta z dzielenia ** do potegi

    c = 1.6
    d = 5
    e = 20
    f = e/d * c
    g = d**2
    # importowac biblioteki - alt enter
    pierwiastek = math.sqrt(20, ) # pierwiastek
    print(str(e) +  str(f)) # str mapowanie
    print(g)

    # listy to tablice zadeklarowane jako ciąg elementów.
    # WAZNE! Indeks w tablicy zaczyna się od 0
    # W związku z tym ostatni indeks jest zawsze o 1 mniejszy niż długość tablicy
    tablica1 = [1, 3, 6, 8]
    tablice3 = [1, "jeden", 6.8]

    for x in tablica1:
        # e = e + x
        e += x
    print(e)

    # dodawanie elemtnów do listy
    tablica1.append(15)
    tablica1.insert(3, 5) # w konkretnym miejscu listy

    message = ""
    tablica_wielowymiarowa = [tablica1, tablice3, ["moja", "nowa", "tablica"]]
    for x in tablica_wielowymiarowa:
        print(x)
        for y in x:
            message +=" " + str(y)
    print(message)

    # slowniki - klucz-wartosc
    # deklaracja słownika - sposob 1
    slownik1 = {}
    slownik1["klucz1"] = 1
    slownik1["klucz2"] = 2
    slownik1["klucz3"] = 3
    print(slownik1.get("klucz5"))

    # deklaracja slownika - sposob 2
    slownik2 = {
        "klucz2": 2,
        "klucz3": 3
    }

    print(slownik1)
    print(slownik2)
    print(slownik2["klucz3"])

    tablica1.append(5)
    # Dodawanie nowych wartości do słownika
    slownik2.update({"klucz4": 4})
    print(slownik2)
    print(tablica1)

    slownik_zagniezdzony = {
        "klucz1": {
            "podklucz1": 1,
            "podklucz2": 2
        },
        "klucz2": {
            "podklucz1": 4,
            "podklucz2": 5
        }
    }

    print(slownik_zagniezdzony["klucz1"]["podklucz1"])

    # Petle
    # For - warunkiem iteracji jest ilosc elementow w zmiennej, po ktorej iterujemy
    for key, value in slownik_zagniezdzony.items():
        print(key + str(value))
        for key2, value2 in value.items():
            print(key2 + ": " + str(value2))

    i = 3

    #While - warunek podajemy przy petle
    while i > 0:
        print("Moja iteracja " + str(i))
        i -= 1

    while True:
        print("moja iteracja " + str(i))
        i += 1
        #break pozwala wyjsc z petli
        if i == 5:
            break

    #Instrukcje warunkowe
    #Operatory logiczne: == (czy jest równe), != (nie jest równe), > >=, < <=
    if i is not None:
        print("cos nie wyszlo")
    else:
        print("Wszystko jest ok")

    i = 0
    if i is None:
        print("cos nie wyszlo")
    elif i == 0:
        print("Podnies wartosc i")
    else:
        print("Wszystko jest ok")

    #instrukcja warunek switch
    #switch(argument):
    #case "Monika":
    #   print("Kobieta")
    #case " Paweł":
    #   print("Męzczyzna")
    #W pythonie realizujemy switch case jako slownik

    slownik_nauczycieli = {
        "biologia": {
            "Imie": "Jan",
            "Nazwisko": "Kowaslki",
            "wiek": 45,
            "miesiac": "Styczen"
        },
        "matematyka": {
            "Imie": "Karol",
            "Nazwisko": "Kowai",
            "wiek": 50,
            "miesiac": "Sierpien"
        },
        "polski": {
            "Imie": "Janina",
            "Nazwisko": "Kowaslka",
            "wiek": 30,
            "miesiac": "Listopad"
        }
    }

    przedmiot = "polski"
    print(slownik_nauczycieli.get(przedmiot))

    poryRoku = ["zima", "wiosna", "jesień", "lato"]

    miesiace = {
        "Styczen": poryRoku[0],
        "Luty": poryRoku[0],
        "Marzec": poryRoku[1],
        "Kwiecien": poryRoku[1],
        "Maj": poryRoku[1],
        "Czerwiec": poryRoku[3],
        "Lipiec": poryRoku[3],
        "Sierpien": poryRoku[3],
        "Wrzesien": poryRoku[2],
        "Pazdziernik": poryRoku[2],
        "Listopad": poryRoku[2],
        "Grudzien": poryRoku[0]
    }

    for nauczyciel in slownik_nauczycieli.values():
        print(nauczyciel["Imie"] + " " + nauczyciel["Nazwisko"] + " " + miesiace.get(nauczyciel["miesiac"]))
        if miesiace.get(nauczyciel["miesiac"]) == "zima":
            print(nauczyciel.get("Imie") + ", juz niedlugo Twoje urodziny!")




