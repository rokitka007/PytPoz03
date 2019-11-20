from obiektowosc.Human import Human


class Man(Human):

    def __init__(self, name, surname, age):
        super().__init__("man")
        self.setName(name)
        self.setSurname(surname)
        self.setWiek(age)

    def presentYourStrenght(self):
        strenght = {
            1: "I don't want to talk about strenght",
            2: "I'm strong enough",
            3: "I'm very strong"
        }

        if self.waga <= 50:
            case = 1
        elif 50 < self.waga <= 90:
            case = 2
        else:
            case = 3

        print(strenght.get(case, "Invalid case"))

    def przedstawSie(self):
        super().przedstawSie()
        self.presentYourStrenght()