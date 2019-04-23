import random

class BattleShip:
  def __init__(self, n):
    self.boardSize = n
    self.board = [[0 for i in range(n)] for j in range(n)]
    self.hitMap = [[0 for i in range(n)] for j in range(n)]
    self.ships = {
      "Destroyer": {"size": 2, "rep": "D"},
      "Cruiser": {"size": 3, "rep": "C"}, 
      "Submarine": {"size": 3, "rep": "S"},
      "Battleship": {"size": 4, "rep": "B"},
      "Aircraft Carrier": {"size": 5, "rep": "A"}
    }

    self.shipState = {
      "D": 2,
      "C": 3, 
      "S": 3,
      "B": 4,
      "A": 5
    }

    self.shipRep = {
      "D": "Destroyer",
      "C": "Cruiser",
      "S": "Submarine",
      "B": "Battleship",
      "A": "Aircraft Carrier"
    }
    self.shipCount = 5
    self.directions = ["d", "r"]


  def isValidCoordinate(self, x, y):
    return 0 <= x < self.boardSize and 0 <= y <= self.boardSize

  # check if valid placement
  def validPlacement(self, ship, x, y, direction):
    shipSize = self.ships[ship]["size"]
    if self.isValidCoordinate(x,y):
      if direction == "d" and 0 <= x+shipSize <= self.boardSize:
        if not any([self.board[i][y] for i in range(x, x+shipSize)]):
          return True
      elif direction == "r" and 0 <= y+shipSize <= self.boardSize:
        if not any([self.board[x][i] for i in range(y, y+shipSize)]):
          return True
    return False

  def place_ship(self, ship, x, y, direction):
    shipSize = self.ships[ship]["size"]
    shipRep = self.ships[ship]["rep"]
    if direction == "d":
      for i in range(x, x+shipSize):
        self.board[i][y] = shipRep
    else:
      for i in range(y, y+shipSize):
        self.board[x][i] = shipRep

  def placeAllShipsHuman(self):
    for ship, shipSize in self.ships.items():
      valid = False
      while not valid:
        print("Enter the co-ordinates in the format x,y,direction ('d' for down and 'r' for right) eg. (1,4,d)")
        try:
          x,y,direction = input("Enter co-ordinates and direction where you want to place the {}: ".format(ship)).split(",")      
          x = int(x)
          y = int(y)
        except:
          print("Please enter input in correct format")
          valid = False
        else:
          valid = self.validPlacement(ship, x, y, direction)
          if valid:
            self.place_ship(ship, x, y, direction)
          else:
            print("Location already occupied. Please try again.")
      self.displayBoard()

  def placeAllShipsComputer(self):
    for ship, shipSize in self.ships.items():
      valid = False
      while not valid:
        x = random.randint(0,self.boardSize-1)
        y = random.randint(0,self.boardSize-1)
        direction = self.directions[random.randint(0,1)]
        valid = self.validPlacement(ship, x, y, direction)
        if valid:
          print("Placing {} at ({},{}) in direction {}".format(ship, x, y, direction))
          self.place_ship(ship, x, y, direction)  
      self.displayBoard()

  def hitTarget(self,x,y):
    if self.isValidCoordinate(x,y):
      if self.board[x][y] in self.shipRep:
        print("It was a Hit at ({},{})!".format(x,y))
        rep = self.board[x][y]
        self.shipState[rep]-=1
        if self.shipState[rep] == 0:
          print("{} destroyed!".format(self.shipRep[rep]))
          self.shipCount-=1
        self.board[x][y] = "*"
        return True
      elif self.board[x][y] == 0:
        print("It was a Miss at ({},{})!".format(x,y))
        self.board[x][y] = "."
        return True
    print("Please try again.")
    return False

  def displayBoard(self):
    print("  ", end="")
    for i in range(self.boardSize):
      print("  {} ".format(i), end="")
    print()
    print("  ", end="")
    print('-' * (self.boardSize*4+1))
    for i, row in enumerate(self.board):
      print("{} |".format(i), end=" ")
      print(*row, sep=" | ", end="")
      print(" |")
      print("  ", end="")
      print('-' * (self.boardSize*4+1))


# b = BattleShip(10)
# b.displayBoard()
