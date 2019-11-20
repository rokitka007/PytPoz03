from obiektowosc.Human import Human

class Woman(Human):

    #Nadpisywanie konstruktora klasy bazowej
    def __init__(self):
        #Slowko super pozwala nam odwolac sie do metody z klasy bazowej (w tym wypadku konstruktora)
        super().__init__("woman", 55)
        self.przedstawSie()


    def makeUp(self, duty=False):
        if duty:
            print ("Wait an hour more, I need do my makeUp")
        else:
            print("Ok, I'm ready to go")

    def przedstawSie(self):
        print("I'm woman and my age shouldn't interest you")

    def przedstawSieMilo(self):
        self.przedstawSie()
        super().przedstawSie()
