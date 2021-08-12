import random
import string

class ant:
    name = "dasd"
    role = "asdas"
    inventory = 0
    #def __init__(self, homeX, homeY):
    def __init__(self, gameArray, homeLocationX, homeLocationY):
        #pick random role, either gatherer or worker
        name = "default"
        inventory = 0
        age = 0
        location = None
        deathFlag = False
    def printAntInfo(self):
        print("Name: " + str(self.name) + " " + "Role: " + self.role)
        # + "\n" + "Location: " + str(self.xCoord) + " ," + str(self.yCoord))

class gatherer(ant):
    def __init__(self, gameArray, homeLocationX, homeLocationY):
        #pick random role, either gatherer or worker
        letters = string.ascii_letters
        self.name = "".join(random.choice(letters) for i in range(random.randint(3, 8)))
        self.inventory = 0
        self.age = 0 #ant can die after some number of months
        self.role = "Gatherer"

        #random initial spawning-------------------------------------------------------
        spawnSelect = random.randint(0, 7)
        spawnOptions = (gameArray[homeLocationX][homeLocationY].topLeft, gameArray[homeLocationX][homeLocationY].top, gameArray[homeLocationX][homeLocationY].topRight,
            gameArray[homeLocationX][homeLocationY].left, gameArray[homeLocationX][homeLocationY].right, gameArray[homeLocationX][homeLocationY].bottomLeft, gameArray[homeLocationX][homeLocationY].bottomLeft,
            gameArray[homeLocationX][homeLocationY].bottom, gameArray[homeLocationX][homeLocationY].bottomRight) #tuple of all spawn options
            
        while spawnOptions[spawnSelect].occupied == True: #if the spawn space is occupied
            spawnSelect += 1
            if spawnSelect > 7: #if all the spaces around the nest are occupied. this could let the gatherer wait in the nest until an opening
                break
        
        self.location = spawnOptions[spawnSelect] #sets the spawn location based on the randomly selected spot
        self.location.occupied = True

        self.location.unit = "A" #updates the unit of the selected spawn space to "A"
        #end of spawning-----------------------------------------------------------------------------------------
        
    def action(self):
        #move around map
            #if the element where the ant will move is node.occupied == False, then it can move there, if not then it needs to look somewhere else
            #since each position on the grid is now a node, if the node has a connection to the nodes surrounding it, then it would
            #just need to check for unoccupied connecting nodes
        #if on resource square, collect it
            #if it moves onto a space that has the resource char on it, then it can pick it up
        return

class worker(ant):
    def __init__(self, gameArray, homeLocationX, homeLocationY):
        letters = string.ascii_letters
        self.name = "".join(random.choice(letters) for i in range(random.randint(3, 8)))
        self.inventory = 0
        self.age = 0 #ant can die after some number of months
        self.role = "Worker"
        self.location = gameArray[homeLocationX][homeLocationY]
    def action(self):
        #if enough free resources, build expansion to nest
        return