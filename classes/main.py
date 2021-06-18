from breadth_first import breadth_first


def backtrack_solution(archive, board):
    '''Given the solution board, this function backtracks all taken steps by going through the archive'''
    current_board = board
    backtrack = [current_board]

    # When 0 is found, this means we're back at the starting board and all steps are found
    while archive[current_board] != 0:
        backtrack.append(archive[current_board])
        current_board = archive[current_board]

    # Reverse the backtrack, so the starting board is in the front and the solution is in the back
    backtrack.reverse()
    return backtrack


def main():
    # Solve the current game by using a breadth first algoritm
    solution = breadth_first()

    # Backtrack the archive to find out how many steps were taken to get to the solution board
    archive = backtrack_solution(solution["archive"], solution["board"])
    checked_boards = solution["popped"]

    # Print statistics
    print(f"Looked at {checked_boards} boards")
    print(f"Solved in {len(archive) - 1} steps")    # -1 because the starting board does not count as a step

    # # Print all steps that were taken
    # for board in archive:
    #     print(board)
    #     print()


if __name__ == "__main__":
    main()