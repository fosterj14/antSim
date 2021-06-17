import pygame
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
    rows, cols = (40, 40)
    gameArea = [[0 for i in range(cols)] for j in range(rows)]
    print (gameArea)

window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.geometry("600x600")
window.title("Ant Sim")

gameInfoFrame = Frame(window)
playAreaFrame = Frame(height=600, width=600)


infoLabel = Label(gameInfoFrame, text = "Hive information", foreground="white", background="black")
infoSection = Text(gameInfoFrame, height = 4, width = 35)
hiveInfo = "Workers: " + str(numWorkers) + "\t" + "Year: " + str(year) + "\n" + "Gatherers: " + str(numGatherers) + "\t" + "Month: " + str(month) + "\n" \
    + "Home Location: " + str(homeLocation) + "\t" + "Day: " + str(day)
pauseBtn = Button(master=gameInfoFrame, text="Pause", width=5, height=1, bg="red", fg="white")
tempPlayAreaLabel = Label(playAreaFrame, text="This is where the play area will be", fg="white", bg="black", height=600, width=600)


infoLabel.pack()
infoSection.pack()
infoSection.insert(END, hiveInfo)
pauseBtn.pack()
tempPlayAreaLabel.pack()
infoSection.config(state=DISABLED)


gameInfoFrame.pack(side=TOP)
playAreaFrame.pack()

window.mainloop()