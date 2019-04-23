# BattleShip

BattleShip Game Playing AI. 
AI works by calculating a Probability Density Function at the beginning of every move.
For every location on the board, a probability of containing a ship is calculated, and next move is determined. 

### To Run

    $ python3 playBattleship.py

### Distribution of moves taken to win (100 games on BoardSize of 10x10)

![Distribution](https://raw.githubusercontent.com/parthnagori/BattleShip/master/battleship_hist.png)

![Norm Distribution](https://raw.githubusercontent.com/parthnagori/BattleShip/master/norm_battleship.png)

Average number of moves to win: 50

