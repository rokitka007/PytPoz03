
def wyswietlZyczenia(*args):
    message = "Moj drogi, zycze Ci"
    for arg in args:
        #Formatowanie stringow (brackety w stringu takie same jak w slowniku)
        message += " {},".format(arg)
    return message

def stworzReprezentanta(**kwargs):
    message = "Twoj reprezentant to: "
    for key, value in kwargs.items():
        # \n to znak specjalny, oznacza przejście do nowej linii (tak jakby wcisnąć enter)
        message += "\n {}: {}".format(key, value)
    return message


if __name__ == '__main__':
    print("Hello")

    # Wykorzystanie *args w funkcjach
    zyczenia1 = wyswietlZyczenia()
    print(zyczenia1)

    zyczenia2 = wyswietlZyczenia("zdrowia", "szczescia", "pomyslnosci")
    print(zyczenia2)

    # Wykorzystanie **kwargs w funkcjach
    reprezentant1 = stworzReprezentanta()
    print(reprezentant1)
    reprezentant2 = stworzReprezentanta(Imie="Kasia", Nazwisko="Kowalska", Wiek=20, Specjalnosc="Funkcje")
    print(reprezentant2)
    reprezentant3 = stworzReprezentanta(Gatunek="Pies", Imie="Poker", Rasa="Owczarek niemiecki", Szkolenia="Brak")
    print(reprezentant3)