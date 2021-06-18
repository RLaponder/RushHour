# RushHour
This program aims to find a solution to multiple RushHour game boards, using a breadth first search algorihm.

## Folders
### classes
This folder contains all Python files.
* board.py
* breadth_first.py
* car.py
* dbconnection.py
* game.py
* main.py

### database
This folder contains the database and a logfile of how it was created and filled.
* databaseCreation.sql
* rushhour.db

### visualizations
This folder contains images of the starting game boards, and an animation of the breadth first solution of game1.

## How to use
Navigate into the classes folder and type in the terminal
'python main.py'
You will be asked which game you would like to solve and you will be shown the options to choose from.
The program will now try to solve this puzzle and once a solution is found, you will be shown how many
board configurations were looked at and how many steps it took to go from the starting board to the final solution.
