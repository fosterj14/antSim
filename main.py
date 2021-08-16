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
year = 1
month = 1
day = 0
count = 0
antList = []

def gameArray():
    rows, cols = (30, 70)
    #gameArea = [["-" for i in range(cols)] for j in range(rows)]

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

    gameArea[homeLocationX][homeLocationY].unit = "H"
    gameArea[homeLocationX][homeLocationY].occupied = True

    #testing the mapping of adjoining nodes
    #gameArea[homeLocationX][homeLocationY].topLeft.unit = "TL"
    #gameArea[homeLocationX][homeLocationY].top.unit = "T"
    #gameArea[homeLocationX][homeLocationY].topRight.unit = "TR"
    #gameArea[homeLocationX][homeLocationY].left.unit = "L"
    #gameArea[homeLocationX][homeLocationY].right.unit = "R"
    #gameArea[homeLocationX][homeLocationY].bottomLeft.unit = "BL"
    #gameArea[homeLocationX][homeLocationY].bottom.unit = "B"
    #gameArea[homeLocationX][homeLocationY].bottomRight.unit = "BR"
    #-------------------------------------------------

    return gameArea

def updateGameArea(day, month, year):
    print("update") #testing
    #Time management
    day = day + 1
    if (day%31 == 0):
        month = month + 1
    if (month%13 == 0 and day%31 == 0):
        year = year + 1

    if day % 5 == 0:
        spawnResources() #this will add new resorces to the map

    #ant action call here
    for ants in antList:
        ants.action()
        ants.age = ants.age + 1
        if (ants.age >= 250):
            antList.remove(ants)

    str2 = ""
    for ele in gameArray: #gets the updated array info
        for ele2 in ele:
            str2 += str(ele2.unit)
            str2 += " "
        str2 += "\n"
    str2 = str2.rstrip("\n")

    playAreaText.config(text=str2, fg = "white", bg = "black", font='Helvetica 12 bold') #updates the play area

    infoText = "Workers: " + str(numWorkers) + "\t" + "Year: " + str(year) + "\n" + "Gatherers: " + str(numGatherers) + "\t" + "Month: " + str(month) + "\n" \
    + "Home Location: " + str(homeLocationX) + " ," + str(homeLocationY) + "\t" + "Day: " + str(day)
    infoSection.config(text = infoText) #updates the hive info

    if day % 20 == 0:
        #randomly select the type of ant
        antList.append(ant.gatherer(gameArray, homeLocationX, homeLocationY))
        #update the number of ants here

    window.after(100, updateGameArea, day, month, year) #calls updateGameArea every 1000 msec

def spawnResources():
    #spawn resources in random areas
        #needs to check for unit collision
    resourceX = randint(0, 29)
    resourceY = randint(0, 69)

    #gameArray[resourceX][resourceY].occupied = True #can't be occupied since ant needs to go on it
    gameArray[resourceX][resourceY].unit = "R"

#Initializes the game window------------------------------------------------------------------------------------------
window = Tk()
backgroundImg = PhotoImage("antPic.jpg")
window.resizable(width=FALSE, height=FALSE)
window.geometry("1000x800")
window.title("Ant Sim")
#---------------------------------------------------------------------------------------------------------------------

backgroundImg = PhotoImage(file = 'E:\\python_work\\antSim\\antPic.PNG')
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
    + "Home Location: " + str(homeLocationX) + " ," + str(homeLocationY) + "\t" + "Day: " + str(day)

infoSection = Label(gameInfoFrame, text = hiveInfo, height = 4, width = 35)

pauseBtn = Button(master=gameInfoFrame, text="Pause", width=5, height=1, bg="red", fg="white")

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
print("Printing info...")
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