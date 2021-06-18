from dbconnection import sql

db = sql()

class Car:
    def __init__(self, dbcar):
        self.name = dbcar["name"]
        self.position_x = dbcar["position_x"]
        self.position_y = dbcar["position_y"]
        self.length = dbcar["length"]
        self.orientation = dbcar["orientation"]
        self.positions = self.set_positions()

    def set_positions(self):
        # Determine the positions of a car, based on the starting position, orientation and length
        self.positions = []
        if self.orientation == "H":
            for i in range(self.length):
                self.positions.append({"x": self.position_x + i, "y": self.position_y})

        elif self.orientation == "V":
            for j in range(self.length):
                self.positions.append({"x": self.position_x, "y": self.position_y + j})

        return self.positions


    def __str__(self):
        return f"Car: {self.name},\nPosition x: {self.position_x},\nPosition y: {self.position_y},\nLength: {self.length},\nOrientation: {self.orientation}"
