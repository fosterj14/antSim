import pygame
from tkinter import *
import ant
#https://realpython.com/python-gui-tkinter/

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
window.geometry("600x600")

infoLabel = Label(text = "Hive information", foreground="white", background="black")
infoSection = Text(window, height = 4, width = 35)
hiveInfo = "Workers: " + str(numWorkers) + "\t" + "Year: " + str(year) + "\n" + "Gatherers: " + str(numGatherers) + "\t" + "Month: " + str(month) + "\n" \
    + "Home Location: " + str(homeLocation) + "\t" + "Day: " + str(day)
pauseBtn = Button(text="Pause", width=5, height=1, bg="red", fg="white")

infoLabel.pack()
infoSection.pack()
infoSection.insert(END, hiveInfo)
pauseBtn.pack()
infoSection.config(state=DISABLED)

window.mainloop()