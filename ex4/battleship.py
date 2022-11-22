import helper


def init_board(rows=helper.NUM_ROWS, columns=helper.NUM_COLUMNS):
    """This function intialzaing an empty board"""
    # Using list comprehension to create a list with the sign for empty cell
    # this list will pass as a paramer to a list comprehension to create
    # a matrix
    board = [[helper.WATER for i in range(columns)] for j in range(rows)]
    return board


def check_row_col(row, col, board):
    """ This funcion checks if the rows or columns of specific
    cell are in the board"""
    if row > 99 or col > 26:
        return False
    if row >= len(board) or row < 0 or col >= len(board[0]) or \
            col < 0:
        return False
    else:
        return True


def cell_loc(name):
    """This function gets a string represent a location in the board and
    return the tuple that fits to that location in the board matrix"""
    # Checks if the first value of the string is alphabetic
    # if name not in range(2,4):
    # return None
    if len(name) <= 1 or len(name) > 3:
        return None
    if name[0].isalpha() == False:
        return None
    else:
        # If yes checks the last of the input can be cast to int
        for i in range(1, len(name)):
            if helper.is_int(name[i]) == False:
                return None
    column = name[0].upper()
    row = int(name[1:]) - 1
    column = (ord(column) % 65)
    return row, column


def valid_ship(board, size, loc):
    """This function gets a board size of a ship and a location indicates
    the start of the ship and return if its possible to put it in the board"""
    row = loc[0]
    col = loc[1]
    if row + size > len(board):
        return False
    for i in range(size):
        if board[row + i][col] == helper.SHIP:
            return False
    return True


def create_player_board(rows=helper.NUM_ROWS,
                        columns=helper.NUM_COLUMNS, ship_sizes=helper.SHIP_SIZES):
    """This function sets submrines in specifics sides in location the user 
    choose, if location is not valid the function will ask for another one"""
    board = init_board(rows, columns)  # Initializing an empty board
    # going over the tuple of ships sizes
    for size in ship_sizes:
        # Asking from the user from a valid location until the location
        # provided is valid
        while True:
            helper.print_board(board)
            user_input = helper.get_input(f'Enter the top coordinate for \
ship of size {size}: ')
            loc = cell_loc(user_input)
            if loc == None:
                print("Invalid Format")
                continue
            if check_row_col(loc[0], loc[1], board) is False:
                print("Location is out of bounds")
                continue
            if valid_ship(board, size, loc) == False:
                print("Invalid location")
                continue
            for i in range(size):
                board[loc[0] + i][loc[1]] = helper.SHIP
            break
    return board


def check_avalibale_spots(board, size):
    """This function gets the  board and return a list of tuples, 
    each tuple represent avalibalse spot"""

    st = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == helper.WATER and i + size <= len(board):
                loc = (i, j)
                st.add(loc)
    return st


def create_computer_board(rows=helper.NUM_ROWS,
                          columns=helper.NUM_COLUMNS, ship_sizes=helper.SHIP_SIZES):
    """Gets the player board and chhose a place to put 
    submarines for the computer"""
    board = init_board(rows, columns)
    # Going over the tuple of ship sizes
    for size in ship_sizes:
        # Checking to choose again while the location does not fit to the
        # ship size
        free_spots = check_avalibale_spots(board, size)
        while True:

            cell = helper.choose_ship_location(board, size, free_spots)
            row = cell[0]
            col = cell[1]
            if valid_ship(board, size, cell) != True:
                continue
            else:
                for i in range(size):
                    board[row + i][col] = helper.SHIP
                break
    return board


def fire_torpedo(board, loc):
    """This function gets a board and a location to fire torpado
    and return the result of the hit"""
    row = loc[0]
    col = loc[1]
    if check_row_col(row, col, board) == False or  \
            board[row][col] == helper.HIT_WATER\
            or board[row][col] == helper.HIT_SHIP:
        return board
    if board[row][col] == helper.SHIP:
        board[row][col] = helper.HIT_SHIP
    else:
        board[row][col] = helper.HIT_WATER
    return board


def game_finished(board):
    """Checks if thera are ships in the board
    to detemine if the game finished"""

    for row in board:
        for item in row:
            if item == helper.SHIP:
                return False
    return True


def turpedo_spots(board):
    """This function gets the player board and return a list of tuples, 
    each tuple represent avalibalse spot to shot turpedo"""
    st = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == helper.WATER:
                loc = (i, j)
                st.add(loc)
    return st


def set_hidden_board(computer_board):
    """Gets the computer board and returns an hidden board. represen ships as 
    water."""
    hidden_board = init_board(len(computer_board), len(computer_board[0]))
    for i in range(len(computer_board)):
        for j in range(len(computer_board[i])):
            if computer_board[i][j] != helper.SHIP:
                hidden_board[i][j] = computer_board[i][j]
            else:
                hidden_board[i][j] = helper.WATER
    return hidden_board


def main():
    """Runs the game"""
    play = 'Y'
    while play == 'Y':
        player_board = create_player_board(
        )  # Creating the user board
        computer_board = create_computer_board(
        )  # Creating the computer board
        hidden_board = set_hidden_board(
            computer_board)  # Hiding the computer ships
        run_game = True  # Boolean value to running the game
        # Loops until game over
        while run_game:
            # The player move
            while True:
                hidden_board = set_hidden_board(computer_board)
                helper.print_board(player_board, hidden_board)
                hit = helper.get_input("Enter a target to hit: ")
                if cell_loc(hit) == None:
                    print("Invalid format")
                    continue
                else:
                    loc = cell_loc(hit)
                    if check_row_col(loc[0], loc[1], computer_board) == False:
                        print("location out of bounds")
                        continue
                    if computer_board[loc[0]][loc[1]] == helper.HIT_WATER\
                            or computer_board[loc[0]][loc[1]] == helper.HIT_SHIP:
                        print("You already choosed this location.")
                        continue
                    else:
                        fire_torpedo(computer_board, loc)
                # The computer move

                player_hidden = set_hidden_board(player_board)
                lst_turpedo = turpedo_spots(player_hidden)
                hit = helper.choose_torpedo_target(player_hidden, lst_turpedo)
                fire_torpedo(player_board, hit)
                break

            # Checks if it's a tie
            if game_finished(player_board) and game_finished(computer_board):
                helper.print_board(player_board, computer_board)
                # take input to check if the user wants to play another round
                while True:
                    answer = helper.get_input("It's a tie, would you \
like to play another round ('Y' = yes, 'N' = no): ")
                    if answer != 'Y' and answer != 'N':
                        print("invalid answer")
                    else:
                        run_game = False
                        break
            # if the computer loses
            elif game_finished(computer_board):
                helper.print_board(player_board, computer_board)
                # take input to check if the user wants to play another round
                while True:
                    answer = helper.get_input("you are the winner, would you \
like to play another round ('Y' = yes, 'N' = no): ")
                    if answer != 'Y' and answer != 'N':
                        print("invalid answer")
                    else:
                        run_game = False
                        break
             # Checks if the player wins
            elif game_finished(player_board):
                helper.print_board(player_board, computer_board)
                # take input to check if the user wants to play another round
                while True:
                    answer = helper.get_input("The computer won, would you \
like to play another round ('Y' = yes, 'N' = no): ")
                    if answer != 'Y' and answer != 'N':
                        print("invalid answer")
                    else:
                        run_game = False
                        break
        play = answer


if __name__ == "__main__":
    main()
