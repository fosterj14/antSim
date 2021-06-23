import random
import string

class ant:
    name = "dasd"
    role = "asdas"
    inventory = 0
    def __init__(self):
        #pick random role, either gatherer or worker
        name = (random.choice(letters) for i in range(random.randint(3, 8)))
        inventory = 0
        age = 0
    def printAntInfo(self):
        print("Name: " + str(self.name) + " " + "Role: " + self.role + "\n")

class gatherer(ant):
    def __init__(self):
        #pick random role, either gatherer or worker
        letters = string.ascii_letters
        self.name = "".join(random.choice(letters) for i in range(random.randint(3, 8)))
        self.inventory = 0
        self.age = 0
        self.role = "Gatherer"
    def action():
        #move around map
        temp = ""
        #if on resource square, collect it

class worker(ant):
    def __init__(self):
        letters = string.ascii_letters
        self.name = "".join(random.choice(letters) for i in range(random.randint(3, 8)))
        self.inventory = 0
        self.age = 0
        self.role = "Worker"
    def action():
        temp = ""
        #if enough free resources, build expansion to nest