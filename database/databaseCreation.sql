-- Create table with boards
CREATE TABLE boards (
    id INTEGER NOT NULL PRIMARY KEY,
    rows INT NOT NULL,
    columns INT NOT NULL
);

-- Insert boards into boards table
INSERT INTO boards (rows, columns)
VALUES (6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12);

-- Create table games
CREATE TABLE games (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(7) NOT NULL,
    board INT NOT NULL,
    FOREIGN KEY(board) REFERENCES boards(id)
);

-- Create Game1
INSERT INTO games (name, board)
VALUES ("game1",
    (SELECT id FROM boards
    WHERE rows = 6
    AND columns = 6)
);

-- Create Game2
INSERT INTO games (name, board)
VALUES ("game2",
    (SELECT id FROM boards
    WHERE rows = 6
    AND columns = 6)
);

-- Create Game3
INSERT INTO games (name, board)
VALUES ("game3",
    (SELECT id FROM boards
    WHERE rows = 6
    AND columns = 6)
);

-- Create table for cars
CREATE TABLE cars (
    id INTEGER PRIMARY KEY NOT NULL,
    game INT NOT NULL,
    name CHAR(1) NOT NULL,              -- Every car is represented by a letter, the red car is always X
    position_x INT NOT NULL,            -- Starting horizontal position on the board
    position_y INT NOT NULL,            -- Starting vertical position on the board
    length INT NOT NULL,                -- Length of the car, can by 2 or 3
    orientation CHAR(1) NOT NULL,        -- Can this car move horizontally or vertically
    FOREIGN KEY(game) REFERENCES games(id)
);

-- Create cars for game1
INSERT INTO cars (game, name, position_x, position_y, length, orientation)
VALUES (1, "A", 2, 0, 3, "V"),
(1, "B", 3, 0, 2, "H"),
(1, "C", 5, 0, 3, "V"),
(1, "X", 3, 2, 2, "H"),
(1, "D", 3, 3, 3, "V"),
(1, "E", 4, 3, 2, "H"),
(1, "F", 0, 4, 2, "V"),
(1, "G", 1, 4, 2, "H"),
(1, "H", 4, 5, 2, "H");

-- Create table to save solution statistics
CREATE TABLE solutions (
    id INTEGER PRIMARY KEY NOT NULL,
    game INT NOT NULL,                  -- Which game was solved
    played INT NOT NULL,                -- How many times was this game solved
    min_moves INT NOT NULL,             -- What was the lowest number of moves to find a solution
    max_moves INT NOT NULL,             -- What was the highest number of moves to find a solution
    avg_moves INT NOT NULL,             -- What was the average number of moves to find a solution
    FOREIGN KEY(game) REFERENCES games(id)
);