from tkinter import *
import ant
#https://realpython.com/python-gui-tkinter/

numWorkers = 0
numGatherers = 0
homeLocation = 0 #this will be a coordinate in the array
year = 1
month = 1
day = 1
count = 0
antList = []

def gameArray():
    rows, cols = (10, 50)
    gameArea = [[0 for i in range(cols)] for j in range(rows)]
    return gameArea

def updateGameArea(): #this will be called once after the ant action phase
    #global count #testing
    #gameArray[count%10][count%49] = 'X' #testing
    #go through the list of ants and call their action function
    print("update") #testing
    str2 = ""
    for ele in gameArray:
        for ele2 in ele:
            str2 += str(ele2)
        str2 += "\n"
    playAreaText.config(text=str2)
    #count +=1 #testing
    window.after(1000, updateGameArea) #this can be moved to the ant action method

#Initializes the game window------------------------------------------------------------------------------------------
window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.geometry("600x600")
window.title("Ant Sim")
#---------------------------------------------------------------------------------------------------------------------

gameArray = gameArray()

#Create GUI elements---------------------------------------------------------------------------------------------------
gameInfoFrame = Frame(window)
playAreaFrame = Frame(height=600, width=600)

infoLabel = Label(gameInfoFrame, text = "Hive information", foreground="white", background="black")

infoSection = Text(gameInfoFrame, height = 4, width = 35)

#need to format text in label here
hiveInfo = "Workers: " + str(numWorkers) + "\t" + "Year: " + str(year) + "\n" + "Gatherers: " + str(numGatherers) + "\t" + "Month: " + str(month) + "\n" \
    + "Home Location: " + str(homeLocation) + "\t" + "Day: " + str(day)

pauseBtn = Button(master=gameInfoFrame, text="Pause", width=5, height=1, bg="red", fg="white")

playAreaText = Label(playAreaFrame)
#------------------------------------------------------------------------------------------------------------------------

#prints the array to the text area
str1 = ""
for ele in gameArray:
    for ele2 in ele:
        str1 += str(ele2)
    str1 += "\n"
playAreaText.config(text=str1)
#------------------------------------------

#Create the starting ants------------------------------
antList.append(ant.gatherer())
antList.append(ant.worker())
print("Printing info...")
print(antList)
for ant in antList:
    ant.printAntInfo()
#------------------------------------------------------

#Loads UI elements------------------------------------
infoLabel.pack()
infoSection.pack()
infoSection.insert(END, hiveInfo)
pauseBtn.pack()
playAreaText.pack()

infoSection.config(state=DISABLED)
playAreaText.config(state=DISABLED, bg="white", fg="black")

gameInfoFrame.pack(side=TOP)
playAreaFrame.pack()
#------------------------------------------------------

updateGameArea()
window.mainloop()