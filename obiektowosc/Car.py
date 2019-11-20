class Car():

    def __init__(self, brand, model, year=2000):
        self.brand = brand
        self.model = model
        self.year = year
        self.velocity = 0

    def presentCar(self):
        message = "{} {} created in {}".format(self.brand, self.model, self.year)
        if 2019-self.year >= 20:
            message += "\nWaiting for destruction"
        print(message)
        return message

    def accelerate(self, velocity):
        self.velocity += velocity

    def brake(self, velocity):
        if self.velocity == 0:
            print("You're not already driving")
        elif self.velocity - velocity < 0:
            self.velocity = 0
        else:
            self.velocity -= velocity

    #Wbudowane funkcje zawsze sa otoczone dwoma podkreslnikami
    # Mozna je nadpisywac - przyklad ponizej
    # Sluza one do interpretowania przez funkcje wbudowane w pythona, takie jak str(), sorted()
    def __str__(self):
        return self.presentCar()

