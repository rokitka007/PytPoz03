import random

if __name__ == '__main__':

    lista1 = []
    # Losowanie generycznych liczb z zakresu a, b przy pomocy funkcji randint modułu random
    for i in range(20):
        lista1.append(random.randint(1, 15))
    print(lista1)
    print(len(lista1))
    zbior = {"a", "b"} # elementy nie moga sie powtarzac, nie sa posortowane
    slownik = {"a": 1,
               "b" : 2}

    slownik.update({"c":3})
    zbior.update({"c"})
    print(zbior)

    # Narzucanie struktury danych: zbior, lista, slownik, krotka
    zbior = set()
    zbior2 = list()
    zbior3 = dict()
    zbior4 = tuple()

    for i in range(20):
        zbior.update({random.randint(10, 25)})
    print(zbior)
    print(len(zbior))

    suma = zip(reversed(lista1), sorted(zbior))
    print(suma)
    print(list(suma))

    for el1, el2 in zip(reversed(lista1), sorted(zbior)):
        print("element1 " + str(el1))

    # Na slownikach nie da sie wykonac funkcji reversed
    # Sortowanie slownikow polega na posortowaniu ich kluczy.
    print(sorted(slownik))