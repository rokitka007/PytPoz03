from obiektowosc.Car import Car
import random

from obiektowosc.Man import Man
from obiektowosc.Tir import Tir

if __name__ == '__main__':

    auto1 = Car("opel", "astra", 2010)
    auto1.presentCar()
    auto1.accelerate(20)
    auto1.brake(30)
    print(auto1.velocity)

    auto2 = Car("bmw", "m3", 1998)
    auto2.presentCar()
    auto2.brake(10)
    auto2.accelerate(30)
    auto2.brake(10)
    print(auto2.velocity)


    tir = Tir("MAN", "123", 2500, 1995)
    owner = Man("Jan", "Kowalski", 45)
    tir.setOwner(owner)
    tir.presentCar()
    tir.setOwner(auto2)
    tir.presentCar()




