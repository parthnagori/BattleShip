# from battleship import BattleShip
from game import Game

if __name__ == "__main__":
  while True:
    try:
        boardSize = input("Enter Board Size: ")
        boardSize = int(boardSize)
    except ValueError:
        print("Please enter a valid integer input")
        continue
    else:
        if boardSize < 5:
          print("Please enter a larger Board Size")
          continue
        else:
          break
  
  player1 = input("Enter Player 1 Name (Press Enter to play as CPU): ")
  player2 = input("Enter Player 2 Name (Press Enter to play as CPU): ")
  if not player1:
    game = Game(boardSize, "CPU1", "CPU2")
  elif not player2:
    game = Game(boardSize, player1, "CPU1")
  else:
    game = Game(boardSize, player1, player2)

  game.playGame()


  # Uncomment to play multiple CPU games in a go
  
  # allGames = []
  # for i in range(100):
  #   print("Game : ", i)
  #   game = Game(10, "CPU1", "CPU2")
  #   moves = game.playGame()
  #   allGames.append(moves)

  # import matplotlib.pyplot as plt
  # plt.xlabel('Number of Moves')
  # plt.ylabel('Count')
  # plt.hist(allGames, facecolor='blue', edgecolor='black',linewidth=1.2)
  # plt.show()



