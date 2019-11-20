from obiektowosc.Human import Human
from obiektowosc.Man import Man
from obiektowosc.Woman import Woman

if __name__ == '__main__':
    # Wykorzystanie klasy Human
    # Tworzenie obeiktu - wolamy klasy tak jak metode (zeby od razu wykonal sie konstruktor, czyli metoda init).
    # Stad potrzebne sa nawiasy za nazwa klasy przy chlopiec=Human()
    chlopiec = Human("boy")
#    chlopiec.przedstawSie()

    chlopiec.setName("Jan")
    chlopiec.setSurname("Kowalski")
    chlopiec.setWiek(13)

  #  chlopiec.przedstawSie()

    #Tworzenie kolejnego obiektu klasy Human
    dziewczynka = Human("girl", 40)
    dziewczynka.setName("Gosia")
    dziewczynka.setSurname("Piotrowska")
    dziewczynka.setWiek(10)

 #   dziewczynka.przedstawSie()

    #Tworzymy obiekt klasy Woman dziedziczacy po Human
    kobieta = Woman()
    kobieta.setName("Agata")
    kobieta.setSurname("Kowalska")
    kobieta.setWiek(32)
    kobieta.przedstawSieMilo()
    kobieta.makeUp(True)

    # Tworzymy obiket klasy Man dziedziczacy po klasie Human
    mezczyzna = Man("Jacek", "Nowicki", 36)
    mezczyzna.przedstawSie()
    mezczyzna.waga = 60
    mezczyzna.przedstawSie()
    mezczyzna.waga = 100
    mezczyzna.przedstawSie()
