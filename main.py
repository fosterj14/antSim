from tkinter import *
from random import seed
from random import randint
import ant
#https://realpython.com/python-gui-tkinter/

numWorkers = 1
numGatherers = 1
homeLocationX = 0 #this will be a coordinate in the array
homeLocationY = 0
year = 1
month = 1
day = 0
yearChange = True
count = 0
antList = []

def gameArray():
    rows, cols = (30, 70)
    gameArea = [["-" for i in range(cols)] for j in range(rows)]
    homeLocationX = randint(0, 30)
    homeLocationY = randint(0, 70)
    gameArea[homeLocationX][homeLocationY] = "H"
    return gameArea

def updateGameArea(day, month, year, yearChange):
    print("update") #testing
    #Time management
    day = day + 1
    if (day%31 == 0):
        month = month + 1
    if (month%13 == 0 and day%31 == 0):
        year = year + 1
        yearChange = True

    #ant action call here
    for ant in antList:
        ant.action()

    str2 = ""
    for ele in gameArray:
        for ele2 in ele:
            str2 += str(ele2)
            str2 += " "
        str2 += "\n"
    str2 = str2.rstrip("\n")

    playAreaText.config(text=str2, fg = "white", bg = "black", font='Helvetica 12 bold')

    infoText = "Workers: " + str(numWorkers) + "\t" + "Year: " + str(year) + "\n" + "Gatherers: " + str(numGatherers) + "\t" + "Month: " + str(month) + "\n" \
    + "Home Location: " + str(homeLocationX) + " ," + str(homeLocationY) + "\t" + "Day: " + str(day)
    infoSection.config(text = infoText)

    window.after(1000, updateGameArea, day, month, year, yearChange)

#Initializes the game window------------------------------------------------------------------------------------------
window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.geometry("1000x800")
window.title("Ant Sim")
#---------------------------------------------------------------------------------------------------------------------

gameArray = gameArray()

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
        str1 += str(ele2)
    str1 += "\n"
str1 = str1.rstrip("\n")
playAreaText.config(text=str1)
#---------------------------------------------------------

#Create the starting ants------------------------------
antList.append(ant.gatherer(homeLocationX, homeLocationY))
antList.append(ant.worker(homeLocationX, homeLocationY))
print("Printing info...")
for ant in antList:
    ant.printAntInfo()
#------------------------------------------------------

#Loads UI elements------------------------------------
infoLabel.pack()
infoSection.pack()
pauseBtn.pack()
playAreaText.pack()

infoSection.config(state=DISABLED)
playAreaText.config(state=DISABLED, bg="white", fg="black")

gameInfoFrame.pack(side=TOP)
playAreaFrame.pack()
#------------------------------------------------------

updateGameArea(day, month, year, yearChange)
window.mainloop()