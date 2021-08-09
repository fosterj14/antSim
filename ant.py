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
        deathFlag = False
    def printAntInfo(self):
        print("Name: " + str(self.name) + " " + "Role: " + self.role + "\n" + "Location: " + str(self.xCoord) + " ," + str(self.yCoord))

class gatherer(ant):
    def __init__(self, homeX, homeY):
        #pick random role, either gatherer or worker
        letters = string.ascii_letters
        self.name = "".join(random.choice(letters) for i in range(random.randint(3, 8)))
        self.inventory = 0
        self.age = 0 #ant can die after some number of months
        self.role = "Gatherer"
        self.xCoord = homeX
        self.yCoord = homeY
    def action(self):
        #move around map
            #if the element of where the and will move is "-", then it can move there, if not then it needs to look somewhere else
        #if on resource square, collect it
            #if it moves onto a space that has the resource char on it, then it can pick it up
        return

class worker(ant):
    def __init__(self, homeX, homeY):
        letters = string.ascii_letters
        self.name = "".join(random.choice(letters) for i in range(random.randint(3, 8)))
        self.inventory = 0
        self.age = 0 #ant can die after some number of months
        self.role = "Worker"
        self.xCoord = homeX
        self.yCoord = homeY
    def action(self):
        #if enough free resources, build expansion to nest
        return