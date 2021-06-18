from dbconnection import sql
import math

db = sql()

class Board:
    def __init__(self, game, cars):
        # For game, rows and columns, query from the database, fetchone because we only expect one result, convert the returned row to a dict and get the value by giving the key
        self.game = dict(db.execute("SELECT id FROM boards WHERE id = (SELECT board FROM games WHERE name = ?)", (game.game,)).fetchone())["id"]
        
        # Initialize dimensions of the board for this game
        self.rows = dict(db.execute("SELECT rows FROM boards WHERE id = ?", (self.game,)).fetchone())["rows"]
        self.columns = dict(db.execute("SELECT columns FROM boards WHERE id = ?", (self.game,)).fetchone())["columns"]
        
        # Draw an empty board
        self.board = self.draw_board()
        
        # Place cars on the board
        self.cars = cars
        self.place_cars()
        
        # Determine where the exit for this board should be; for uneven heights it's in the middle, for even heights it's one above the middle
        self.exit = {"x": (self.columns - 1), "y": (math.ceil(self.rows / 2) - 1)}

        # Determine if the current board is a solutions (this means the red car "X" is in front of the exit)
        self.solved = self.is_solved()


    def draw_board(self):
        # Place all 0's on the board
        self.board = [[0 for x in range(self.columns)] for y in range(self.rows)]
        return self.board


    def place_cars(self):
        # Place the car's letter on the board
        for car in self.cars:
            for position in car.positions:
                self.board[position["y"]][position["x"]] = car.name


    def is_solved(self):
        """If the board exit position is in the positions list of the red car ("X"), the game is solved"""
        # Get red car from cars list (red car is always named "X")
        for car in self.cars:
            if car.name == "X":
                red_car = car

        # Get the exit position for this board. If the red car is on this position, the car can exit the board and the board is solved
        if self.exit in red_car.positions:
            # Show the board with all cars in their ending positions and return True
            return True

        # The red car is not on the exit position, return False
        return False


    def __str__(self):
        # Return a visualization of the board
        return "\n".join([" ".join(str(row)) for row in self.board])
