from tkinter import *
from random import seed
from random import randint
import ant
import node
#https://realpython.com/python-gui-tkinter/

numWorkers = 1
numGatherers = 1
homeLocationX = randint(0, 29) #this will be a coordinate in the array
homeLocationY = randint(0, 69)
home = (homeLocationX, homeLocationY)
year = 1
month = 1
day = 0
count = 0
maxAnts = 10
antList = []
paused = FALSE
food = [0]

def pauseCallback():
    global paused
    paused = not paused

def gameArray():
    rows, cols = (30, 70)

    gameArea = [[node.node() for i in range(cols)] for j in range(rows)]
    
    #this sets the connecting nodes for each space
    for i in range(len(gameArea)):
        for j in range(len(gameArea[i])):
            gameArea[i][j].topLeft = gameArea[(i-1)%rows][(j-1)%cols]
            gameArea[i][j].top = gameArea[(i-1)%rows][(j)%cols]
            gameArea[i][j].topRight = gameArea[(i-1)%rows][(j+1)%cols]
            gameArea[i][j].left = gameArea[(i)%rows][(j-1)%cols]
            gameArea[i][j].right = gameArea[(i)%rows][(j+1)%cols]
            gameArea[i][j].bottomLeft = gameArea[(i+1)%rows][(j-1)%cols]
            gameArea[i][j].bottom = gameArea[(i+1)%rows][(j)%cols]
            gameArea[i][j].bottomRight = gameArea[(i+1)%rows][(j+1)%cols]
            gameArea[i][j].coord = (i,j)

    gameArea[homeLocationX][homeLocationY].unit = "H"
    gameArea[homeLocationX][homeLocationY].occupied = True

    return gameArea

def updateGameArea(day, month, year):
    global numGatherers
    global paused
    if not paused:
        #Time management
        day = day + 1
        if (day%31 == 0):
            month = month + 1
        if (month%13 == 0 and day%31 == 0):
            year = year + 1
    
        if day % 10 == 0:
            spawnResources() #this will add new resorces to the map
    
        #ant action call here
        for ants in antList:
            ants.age = ants.age + 1
            if (ants.age >= 250):
                ants.die()
                antList.remove(ants)
                numGatherers = numGatherers - 1
                break
            if ants.role == "Gatherer" and ants.full:
                ants.returnHome(gameArray, food)
            else:
                ants.action()
                ants.age = ants.age + 1
    
        str2 = ""
        for ele in gameArray: #gets the updated array info
            for ele2 in ele:
                str2 += str(ele2.unit)
                str2 += " "
            str2 += "\n"
        str2 = str2.rstrip("\n")
    
        playAreaText.config(text=str2, fg = "white", bg = "black", font='Helvetica 12 bold') #updates the play area
    
        infoText = "Workers: " + str(numWorkers) + "\t" + "Year: " + str(year) + "\n" + "Gatherers: " + str(numGatherers) + "\t" + "Month: " + str(month) + "\n" \
        + "Home Location: " + str(homeLocationX) + " ," + str(homeLocationY) + "\t" + "Day: " + str(day) + "\n" + "Food: " + str(food[0])
        infoSection.config(text = infoText) #updates the hive info
    
        if day % 20 == 0:
            #randomly select the type of ant
            if len(antList) <= 10:
                antList.append(ant.gatherer(gameArray, homeLocationX, homeLocationY))
                antList[-1].printAntInfo()
                numGatherers = numGatherers + 1
            #update the number of ants here
    
    window.after(100, updateGameArea, day, month, year) #calls updateGameArea every 1000 msec

def spawnResources():
    resourceX = randint(0, 29)
    resourceY = randint(0, 69)

    gameArray[resourceX][resourceY].unit = "R"

#Initializes the game window------------------------------------------------------------------------------------------
window = Tk()
backgroundImg = PhotoImage("black-ants.jpg")
window.resizable(width=FALSE, height=FALSE)
window.geometry("1000x800")
window.title("Ant Sim")
#---------------------------------------------------------------------------------------------------------------------

canvas = Canvas(window, width = 1000, height = 800)
canvas.create_image(0, 0, image = backgroundImg)

gameArray = gameArray()
spawnResources()

#Create GUI elements---------------------------------------------------------------------------------------------------
gameInfoFrame = Frame(window)
playAreaFrame = Frame(height=600, width=600)

infoLabel = Label(gameInfoFrame, text = "Hive information", foreground="white", background="black")

#need to format text in label here
hiveInfo = "Workers: " + str(numWorkers) + "\t" + "Year: " + str(year) + "\n" + "Gatherers: " + str(numGatherers) + "\t" + "Month: " + str(month) + "\n" \
    + "Home Location: " + str(homeLocationX) + " ," + str(homeLocationY) + "\t" + "Day: " + str(day) + "Food: " + str(food[0])

infoSection = Label(gameInfoFrame, text = hiveInfo, height = 4, width = 35)

pauseBtn = Button(master=gameInfoFrame, text="Pause", width=5, height=1, bg="red", fg="white", command=pauseCallback)

playAreaText = Label(playAreaFrame, fg = "white", bg = "black")
#------------------------------------------------------------------------------------------------------------------------

#prints the array to the text area---------------------
str1 = ""
for ele in gameArray:
    for ele2 in ele:
        str1 += str(ele2.unit)
        str1 += " "
    str1 += "\n"
str1 = str1.rstrip("\n")
playAreaText.config(text=str1)
#---------------------------------------------------------

#Create the starting ants------------------------------
antList.append(ant.gatherer(gameArray, homeLocationX, homeLocationY))
antList.append(ant.worker(gameArray, homeLocationX, homeLocationY))
print("Starting ants: ")
for ants in antList:
    ants.printAntInfo()
#------------------------------------------------------

#Loads UI elements------------------------------------
infoLabel.pack() #just reads "Hive Information"
infoSection.pack() #contains all the info on the hive
pauseBtn.pack() #the pause button
playAreaText.pack() #area where the game array is displayed

infoSection.config(state=DISABLED)
playAreaText.config(state=DISABLED, bg="white", fg="black")

gameInfoFrame.pack(side=TOP)
playAreaFrame.pack()
canvas.pack(fill = "both", expand = True)
#------------------------------------------------------

updateGameArea(day, month, year)
window.mainloop()