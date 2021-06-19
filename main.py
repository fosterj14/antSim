from tkinter import *
import ant
#https://realpython.com/python-gui-tkinter/

#hello from laptop

numWorkers = 0
numGatherers = 0
homeLocation = 0 #this will be a coordinate in the array
year = 1
month = 1
day = 1

def gameArray():
    rows, cols = (40, 50)
    gameArea = [[0 for i in range(cols)] for j in range(rows)]
    return gameArea

def updateGameArea(textArea, gameArray):
    gameArray[0][0] = 'X'
    for ele in gameArray:
        textArea.insert(END, " ", "center")
        for ele2 in ele:
            textArea.insert(END, ele2)
        playAreaText.insert(END, " \n")

window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.geometry("600x600")
window.title("Ant Sim")

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

playAreaText = Text(playAreaFrame)
playAreaText.tag_configure("center", justify="center")
#------------------------------------------------------------------------------------------------------------------------

#prints the array to the text area
for ele in gameArray:
    playAreaText.insert(END, " ", "center")
    for ele2 in ele:
        playAreaText.insert(END, ele2)
    playAreaText.insert(END, " \n")
#------------------------------------------

#Loads UI elements------------------------------------
infoLabel.pack()
infoSection.pack()
infoSection.insert(END, hiveInfo)
pauseBtn.pack()
playAreaText.pack()

infoSection.config(state=DISABLED)
playAreaText.config(state=DISABLED, bg="black", fg="white")

gameInfoFrame.pack(side=TOP)
playAreaFrame.pack()
#------------------------------------------------------

window.mainloop()