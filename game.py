from battleship import BattleShip
import random
class Game:
  def __init__(self, boardSize, player1Name, player2Name):
    self.player1 = BattleShip(boardSize)
    self.player2 = BattleShip(boardSize)
    self.player1Name = player1Name
    self.player2Name = player2Name
    self.boardSize = boardSize

  def fillBoards(self):
    if "CPU" in self.player1Name:
      print("Placing ships for {}".format(self.player1Name))
      self.player1.placeAllShipsComputer()
    else:
      print("{}, please place your ships".format(self.player1Name))
      self.player1.placeAllShipsHuman()
    if "CPU" in self.player2Name:
      print("Placing ships for {}".format(self.player2Name))
      self.player2.placeAllShipsComputer()
    else:
      print("{}, please place your ships".format(self.player2Name))
      self.player2.placeAllShipsHuman()

  def getTargetHuman(self):
    valid = False
    while not valid:
      try:
        x,y = input("Enter target in format x,y: ").split(",")
        x = int(x)
        y = int(y)
      except:
        print("Invalid co-ordinates. Please try again")
      else:
        valid = True
    return x,y

  def getTargetComputer(self, player):
    valid = False
    if player.firstHitMade:
      print("\nMaking AI Move")
      return player.getBestLocation()
    else:
      x = random.randint(0,self.boardSize-1)
      y = random.randint(0,self.boardSize-1)
      return [x,y]

  def playGame(self):
    self.fillBoards()
    player1 = True
    won = False
    c1, c2 = 0, 0
    while not won:
      if player1:
        print("{}'s turn.".format(self.player1Name))
        move = False
        while not move:
          if "CPU" in self.player1Name:
            x,y = self.getTargetComputer(self.player2)
          else:
            x,y = self.getTargetHuman()
          move = self.player2.hitTarget(x,y)
          self.player2.recalculateHitProbabilities()
        player1 = False
        self.player2.displayBoard()
        if self.player2.shipCount == 0:
          print("{} has won".format(self.player1Name))
          won = True
        c1+=1
      else:
        print("{}'s turn.".format(self.player2Name))
        move = False
        while not move:
          if "CPU" in self.player2Name:
            x,y = self.getTargetComputer(self.player1)
          else:
            x,y = self.getTargetHuman()
          move = self.player1.hitTarget(x,y)
          self.player1.recalculateHitProbabilities()
        player1 = True
        self.player1.displayBoard()
        if self.player1.shipCount == 0:
          print("{} has won".format(self.player2Name))
          won = True
        c2+=1
      print("Moves made Player 1 : {} and Player 2: {}".format(c1, c2))