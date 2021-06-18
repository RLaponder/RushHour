from game import Game
from board import Board
import copy
from collections import deque 


def breadth_first():
    # Initialise game
    game = Game()
    cars = game.cars

    # Get starting board with all cars in their starting position
    starting_board = Board(game, cars)

    # Put starting board in double ended queue
    boards_queue = deque()
    boards_queue.appendleft(starting_board)

    # Open archive for board that have been checked
    board_archive = []

    # Open archive to later traverse back in, when solution is found
    trav_archive = {}

    # Put starting board in archive, because this is not the solution    
    board_archive.append(starting_board.board)
    trav_archive[starting_board] = 0

    popped = 0

    # As long as boards queue is not empty, keep adding and checking new board options
    while len(boards_queue) != 0:
        # Pop board from queue (pop takes and removes from the right side of the queue, so FIFO)
        checking_board = boards_queue.pop()
        
        # Counter for how many board configurations have been looked at
        popped += 1
        
        # Check if the current board is a solution
        if checking_board.is_solved():
            return {"board": checking_board, "archive": trav_archive, "popped": popped}

        # If this board is not a solution
        else:
            for board_config in check_moves(checking_board, game):
                # Get board for this configuration
                # If this board configuration has already been looked at, skip it, because it was not a solution
                if board_config.board in board_archive:
                    pass
                # If this board configuration has not yet been looked at, put it in the queue and in the archive
                else:
                    boards_queue.appendleft(board_config)
                    board_archive.append(board_config.board)
                    trav_archive[board_config] = checking_board


def check_moves(checking_board, game):
    board = checking_board
    # Put cars on board
    possible_boards = []
    for car in board.cars:
        # Check orientation of the car
        if car.orientation == "H":
            # Check if move to the left is possible
            if car.position_x - 1 >= 0 and board.board[car.position_y][car.position_x - 1] == 0:
                new_cars = copy.deepcopy(checking_board.cars)
                moved_car = copy.deepcopy(car)

                # Change position of new car
                moved_car.position_x -= 1
                for position in moved_car.positions:
                    position["x"] -= 1

                # Remove old car and place in the moved car
                for new_car in new_cars:
                    if new_car.name == car.name:
                        new_cars.remove(new_car)
                new_cars.append(moved_car)

                # Create a board with these new cars and add to possible boards list
                possible_boards.append(Board(game, new_cars))

            # Check if move to the right is possible
            if car.position_x + car.length <= board.columns - 1 and board.board[car.position_y][car.position_x + car.length] == 0:
                new_cars = copy.deepcopy(checking_board.cars)
                moved_car = copy.deepcopy(car)

                # Change position of new car
                moved_car.position_x += 1
                for position in moved_car.positions:
                    position["x"] += 1

                # Remove old car and place in the moved car
                for new_car in new_cars:
                    if new_car.name == car.name:
                        new_cars.remove(new_car)
                new_cars.append(moved_car)

                # Create a board with these new cars and add to possible boards list
                possible_boards.append(Board(game, new_cars))
        
        elif car.orientation == "V":
            # Check if move up is possible
            if car.position_y - 1 >= 0 and board.board[car.position_y - 1][car.position_x] == 0:
                new_cars = copy.deepcopy(checking_board.cars)
                moved_car = copy.deepcopy(car)

                # Change position of new car
                moved_car.position_y -= 1
                for position in moved_car.positions:
                    position["y"] -= 1

                # Remove old car and place in the moved car
                for new_car in new_cars:
                    if new_car.name == car.name:
                        new_cars.remove(new_car)
                new_cars.append(moved_car)

                # Create a board with these new cars and add to possible boards list
                possible_boards.append(Board(game, new_cars))
            
            # Check if move down is possible
            if car.position_y + car.length <= board.rows - 1 and board.board[car.position_y + car.length][car.position_x] == 0:
                new_cars = copy.deepcopy(checking_board.cars)
                moved_car = copy.deepcopy(car)

                # Change position of new car
                moved_car.position_y += 1
                for position in moved_car.positions:
                    position["y"] += 1

                # Remove old car and place in the moved car
                for new_car in new_cars:
                    if new_car.name == car.name:
                        new_cars.remove(new_car)
                new_cars.append(moved_car)

                # Create a board with these new cars and add to possible boards list
                possible_boards.append(Board(game, new_cars))

    # Return list of boards that represent valid next moves 
    return possible_boards
