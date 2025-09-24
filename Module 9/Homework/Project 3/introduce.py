class robot:
    model = "RX100"
    creator = "Hrishikesh"

    def __init__(self, name):
        self.name = name    

    def introduction(self):
        print("Hi I am a robot.")

    def details(self, name):
        print("My name is", self.name)
        print("My model is", self.model)
        print("I was created by", self.creator)

ob = robot("Robo")
ob.introduction()
ob.details("Robo")