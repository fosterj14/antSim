import random
import string

class ant:
    name = "dasd"
    role = "asdas"
    inventory = 0
    def __init__(self, homeX, homeY):
        #pick random role, either gatherer or worker
        name = "default"
        inventory = 0
        age = 0
        xCoord = homeX
        yCoord = homeY
    def printAntInfo(self):
        print("Name: " + str(self.name) + " " + "Role: " + self.role + "\n" + "Location: " + str(self.xCoord) + " ," + str(self.yCoord))

class gatherer(ant):
    def __init__(self, homeX, homeY):
        #pick random role, either gatherer or worker
        letters = string.ascii_letters
        self.name = "".join(random.choice(letters) for i in range(random.randint(3, 8)))
        self.inventory = 0
        self.age = 0
        self.role = "Gatherer"
        self.xCoord = homeX
        self.yCoord = homeY
    def action(self):
        #move around map
        temp = ""
        #if on resource square, collect it

class worker(ant):
    def __init__(self, homeX, homeY):
        letters = string.ascii_letters
        self.name = "".join(random.choice(letters) for i in range(random.randint(3, 8)))
        self.inventory = 0
        self.age = 0
        self.role = "Worker"
        self.xCoord = homeX
        self.yCoord = homeY
    def action(self):
        temp = ""
        #if enough free resources, build expansion to nest