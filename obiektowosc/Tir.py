from obiektowosc.Car import Car
from obiektowosc.Man import Man


class Tir(Car):

    def __init__(self, brand, model, weight, year=2000):
        super().__init__(brand, model, year)
        self.weight = weight
        self.owner = None

    def accelerate(self, velocity):
        if velocity - 5 < 0:
            self.velocity += velocity
        else:
            self.velocity += velocity-5

    def setOwner(self, owner):
        # isintsance sprawdza, jakiego typu / jakiej struktury jest nasz obiekt
        if not isinstance(owner, Man):
            print("You need to pass here an object of class Man, not other")
            return
        self.owner = owner

    def presentCar(self):
        super().presentCar()
        if self.owner:
            self.owner.przedstawSie()