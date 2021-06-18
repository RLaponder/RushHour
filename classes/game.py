from dbconnection import sql
from car import Car


db = sql()

class Game:
    def __init__(self):
        self.game = self.get_game()
        self.cars = self.load_cars()


    def get_game(self):
        # Get the supported games from db and let user choose a game
        games = [dbgame["name"] for dbgame in [dict(row) for row in db.execute("SELECT name FROM games").fetchall()]]
        self.game = ""
        while not self.game in games:
            print("Which game would you like to solve?")
            self.game = input("Currently supported: game1\n")
        return self.game


    def load_cars(self):
        # Get the game_id so the right cars can be fetched from db
        self.cars = []
        game_id = dict(db.execute("SELECT id FROM games WHERE name = ?", (self.game, )).fetchone())["id"]
        # Get all the cars that belong to the selected game and retrieve them as a dict
        dbcars = [dict(row) for row in db.execute("SELECT * FROM cars WHERE game = ?", (game_id, )).fetchall()]

        # For every car row from db, create a car object and add it to cars list
        for dbcar in dbcars:
            car = Car(dbcar)
            self.cars.append(car)

        return self.cars
