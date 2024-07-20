import random
import string
import numpy as np

class ant:
    name = "dasd"
    role = "asdas"
    inventory = 0
    spawnOptions = 0
    #def __init__(self, homeX, homeY):
    def __init__(self, gameArray, homeLocationX, homeLocationY):
        #pick random role, either gatherer or worker
        name = "default"
        full = False
        age = 0
        location = None
        deathFlag = False
    def printAntInfo(self):
        print("New Ant - Name: " + str(self.name) + " " + "Role: " + self.role)
        # + "\n" + "Location: " + str(self.xCoord) + " ," + str(self.yCoord))

class gatherer(ant):
    def __init__(self, gameArray, homeLocationX, homeLocationY):
        global spawnOptions
        #pick random role, either gatherer or worker
        letters = string.ascii_letters
        self.name = "".join(random.choice(letters) for i in range(random.randint(3, 8)))
        self.full = False
        self.age = 0 #ant can die after some number of months
        self.role = "Gatherer"
        self.home=(homeLocationX,homeLocationY)

        #random initial spawning-------------------------------------------------------
        spawnSelect = random.randint(0, 7)
        spawnOptions = (gameArray[homeLocationX][homeLocationY].topLeft, gameArray[homeLocationX][homeLocationY].top, gameArray[homeLocationX][homeLocationY].topRight,
            gameArray[homeLocationX][homeLocationY].left, gameArray[homeLocationX][homeLocationY].right, gameArray[homeLocationX][homeLocationY].bottomLeft, gameArray[homeLocationX][homeLocationY].bottomLeft,
            gameArray[homeLocationX][homeLocationY].bottom, gameArray[homeLocationX][homeLocationY].bottomRight) #tuple of all spawn options

        #this needs to be revised. %8 the spawnSelect, then have a count for each spot tried. if it counts >7, then the ant can stay in the nest
        while spawnOptions[spawnSelect].occupied == True: #if the spawn space is occupied
            spawnSelect += 1
            if spawnSelect > 7: #if all the spaces around the nest are occupied. this could let the gatherer wait in the nest until an opening
                #print("Ants need to go into nest")
                break
        
        self.location = spawnOptions[spawnSelect] #sets the spawn location based on the randomly selected spot
        self.location.occupied = True

        self.location.unit = "A" #updates the unit of the selected spawn space to "A"
        #end of spawning-----------------------------------------------------------------------------------------

    def die(self):
        self.location.occupied = False
        self.location.unit = "-"
        print(self.name + " died olf old age. They were a " + self.role)

    def returnHome(self, gameArray):
            global spawnOptions
            global food
            if self.location in spawnOptions:
                self.full = False
                self.location.unit = "A"
                #food = food + 1
                #print ("home")
            else:
                moveOptions = (self.location.topLeft.coord, self.location.top.coord, self.location.topRight.coord, self.location.left.coord, self.location.right.coord, 
                               self.location.bottomLeft.coord, self.location.bottomLeft.coord, self.location.bottom.coord, self.location.bottomRight.coord)
                moveOptions = np.array(moveOptions)
                tgt = self.home
                distances = np.linalg.norm(moveOptions-tgt, axis=1)
                min = np.argmin(distances)
                choice = moveOptions[min]
                self.location.occupied = False
                self.location.unit = "-" #two lines to set the old space to empty

                self.location = gameArray[choice[0]][choice[1]] #sets the spawn location based on the randomly selected spot
                self.location.occupied = True
                self.location.unit = "F"

    def action(self):
        #check if the ant needs to return home or not (if full == True)
        if self.full == True:
            self.location.unit = "F"
            #find best path home
            self.returnHome(self)
        else:
        #move around map
            moveSelect = random.randint(0, 7)
            moveOptions = (self.location.topLeft, self.location.top, self.location.topRight, self.location.left, self.location.right, self.location.bottomLeft, 
                self.location.bottomLeft, self.location.bottom, self.location.bottomRight) #tuple of all spawn options

        #this needs to be revised. %8 the spawnSelect, then have a count for each spot tried. if it counts >7, then the ant can stay in the nest
            while moveOptions[moveSelect].occupied == True: #if the spawn space is occupied
                moveSelect += 1
                if moveSelect > 7: #if all the spaces around the nest are occupied. this could let the gatherer wait in the nest until an opening
                    #print("Ant can't move")
                    break

        #if on resource square, collect it
            #if it moves onto a space that has the resource char on it, then it can pick it up
            if moveOptions[moveSelect].unit == "R":
                self.full = True

            self.location.occupied = False
            self.location.unit = "-" #two lines to set the old space to empty

            self.location = moveOptions[moveSelect] #sets the spawn location based on the randomly selected spot
            self.location.occupied = True

            self.location.unit = "A" #updates the unit of the selected spawn space to "A"

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
    def die(self):
        print(ant.name + " died olf old age")