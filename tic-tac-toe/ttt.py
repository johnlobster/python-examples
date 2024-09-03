# Python tic-tac-toe

# Main program - contains view as this uses tkInter with event loop

from tkinter import *
from tkinter import ttk

import tttModel
import tttController

tttClass = tttModel.TTTModel()

print( "Testing the tic tac toe program")



# btn=[[]]
# x=0
# for i in [0,1,2]:
#   for j in [0,1,2]:
#     btn[i].append(x)
#     x = x+1
#   btn.append([])

# for i in [0,1,2]:
#   for j in [0,1,2]:
#     print( btn[i][j])
# newVals = tttClass.getArray()
# print("new values ", newVals)

################################################################################################################
# View: 
# 

def updateView(): # update all text strings in array
  newVal = tttClass.getArray() 
  for i in range(len(tttClass.tttArray)):
    for j in range(len(tttClass.tttArray[0])):
      btnString[i][j].set(newVal[i][j])

def checkWinner(): # check for winner and update string in info window if it is a winner
  isWinner = False
  win = tttClass.isWinner()
  if win[0] != "":
    infoString.set(win[0] + " is the winner")
    # print("Winner ",win[1])
    isWinner = True
  return isWinner

def changeCell( row, column, value):
  #print('changeCell row=', row, " column=",column)
  tttClass.change(row,column, value)
  updateView()
  
  # check to see if there is a winning line
  win = tttClass.isWinner()
  if checkWinner():
    pass
  else:
    # opponent gets a turn
    tttClass.computerTurn()
    checkWinner()

def resetArray():
  print("Reset")
  tttClass.reset()
  updateView()
  infoString.set("Started new game")

# View: create view and Tk event loop

tkRootWindow = Tk()  # Create Tk() class, with window tkRootWindow
tkFrame = ttk.Frame(tkRootWindow, padding=10) # Create frame widget inside rkRootWindow
tkFrame.grid() # geometry manager controls where widgets are placed inside frame



# create array of Tk strings to hold button text
originalValue = tttClass.getArray()
btnString=[[]]
for i in [0,1,2]:
  for j in [0,1,2]:
    x= StringVar()
    btnString[i].append(x)
    btnString[i][j].set(originalValue[i][j])

  btnString.append([])

infoString=StringVar()
infoString.set("Information")

# create the tic tac toe array
tttCell=[[]] # array to hold the buttons, note: have to append new rows as run through creating everything

for i in range(len(tttClass.tttArray)):
  for j in range(len(tttClass.tttArray[0])):
    tttCell[i].append(
      ttk.Button(tkFrame,
        textvariable=btnString[i][j], 
        command=lambda i=i, j=j: changeCell(i,j,"X")).grid(column=j, row=i)) # create button in array


    tttCell.append([])
# created, buttons, now attach command
# for i in range(len(tttClass.tttArray)):
#   for j in range(len(tttClass.tttArray[0])):
#     print("Attach command")
#     tttCell[i][j].config(command=lambda: changeCell(i,j,"Z"))


# View: Name of program, info window, reset and quit button

ttk.Label(tkFrame,
  textvariable=infoString).grid(column=0, row=4)
ttk.Label(tkFrame, 
  text="Tic Tac Toe program").grid(column=0, row=5) # Create text widget
ttk.Button(tkFrame, text="Reset", command=lambda: resetArray() ).grid(column=1, row=5) # create button widget
ttk.Button(tkFrame, 
  text="Quit", command=tkRootWindow.destroy).grid(column=2, row=5) # create button widget

# Run the event loop
tkRootWindow.mainloop() 

# End of view code
################################################################################################################

print(tttClass.tttArray)
print("End of tic tac toe program")


