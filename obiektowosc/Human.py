#Zmienne w skryptach w klasach nazywają się atrybutami
# Funkcje w skryptach w klasach nazywają się metodami

# Deklaracją klasy, czyli repreznetacja modelu rzeczywistosci
class Human():

    #Konstruktor klasy
    #Kiedy dodajemy argumenty z wartascia defaultowa, to musza byc wypisane na koncu listy argumentow
    def __init__(self, sex, waga=50):
        self.name = ""
        self.surname = ""
        self.wiek = 0
        self.sex = sex
        self.waga = waga

    # Settery - metody, które ustawiają wartość atrybutów klasy
    def setName(self, name):
        self.name=name

    def setSurname(self, surname):
        self.surname = surname

    def setWiek(self, wiek):
        self.wiek = wiek

    # Getter - zwraca jakis parametr, nie ingeruja w zadne zmienne
    def getName(self):
        return self.name

    def przedstawSie(self):
        print("I'm {} {} and I'm {} years old. I'm {} and I weight {}".
              format(self.name, self.surname, self.wiek, self.sex, self.waga))


