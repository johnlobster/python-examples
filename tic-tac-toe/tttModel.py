# Python tc tac toe - model definition

import random

class TTTModel:
  # The tt data array - a 3x3 list where each element can be "", "X" or "O"
  defaultArray = [["","",""],["","",""],["","",""]]
  def __init__( self):
    # tttArray is row, column
    self.tttArray = [["","",""],["","",""],["","",""]]
  
  # get the array
  def getArray(self):
    return self.tttArray 
  
  # change a value
  def change(self, row, column, value="X"): 
    self.tttArray[row][column] = value
    #print( "TTTModel:change() Changed row ", row, " column ", column, " to ", value)

  # reset the array
  def reset(self):
    for i in [0,1,2]:
      for j in [0,1,2]:
        self.tttArray[i][j] = ""

  def isWinner(self):
    winner = ("",[]) # Return tuple containing Winning symbol and list of winning locations

    # horizontal row
    for i in [0,1,2]:
      if (self.tttArray[i][0] != "") and (self.tttArray[i][0] == self.tttArray[i][1]) and (self.tttArray[i][1] == self.tttArray[i][2]):
        winner=(self.tttArray[i][0], [[i,0],[i,1],[i,2]])
    # vertical row
    for i in [0,1,2]:
      if (self.tttArray[0][i] != "") and (self.tttArray[0][i] == self.tttArray[1][i]) and (self.tttArray[1][i] == self.tttArray[2][i]):
        winner=(self.tttArray[i][0], [[0,i],[1,i],[2,i]])
    # cross
    if (self.tttArray[0][0] != "") and (self.tttArray[0][0] == self.tttArray[1][1]) and (self.tttArray[1][1] == self.tttArray[2][2]):
      winner=(self.tttArray[0][0], [[0,0],[1,1],[2,2]])
    if (self.tttArray[0][2] != "") and (self.tttArray[0][2] == self.tttArray[1][1]) and (self.tttArray[1][1] == self.tttArray[2][0]):
      winner=(self.tttArray[0][2], [[0,2],[1,1],[2,0]])
    if winner[0] != "":
      print("TTTModel:isWinner() Winner")
    return winner

  # Computer gets a turn, various methods

  # random entry cannot go into an infinite loop so has to find valid locations first
  def randomEntry(self, value="O"):
    validLocations = []
    for i in [0,1,2]:
      for j in [0,1,2]:
        if self.tttArray[i][j] == "":
          validLocations.append([i,j])
    if ( len(validLocations) == 0):
      print("TTTModel:randomEntry() no valid locations")
    else:
      location = random.randrange(len(validLocations))
      self.change(validLocations[location][0], validLocations[location][1],value)
      #print("TTTModel:randomEntry() selected i=",validLocations[location][0]," j=",validLocations[location][1],)

  def computerTurn(self, value="O"):
    self.randomEntry(value)
