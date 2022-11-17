import helper


def init_board(rows = helper.NUM_ROWS, columns = helper.NUM_COLUMNS):
    """This function intialzaing an empty board"""
    # Using list comprehension to create a list with the sign for empty cell
    # this list will pass as a paramer to a list comprehension to create
    # a matrix
    board = [[helper.WATER for i in range(columns)] for j in range(rows)]
    return board

def check_row_col(row, col):
    """ This funcion checks if the rows or columns of specific
    cell are in the board"""
    if row >= helper.NUM_ROWS or row < 0  or col >=  helper.NUM_COLUMNS or \
        col < 0:
        return False
    else:
        return True

def cell_loc(name):
    """This function gets a string represent a location in the board and
    return the tuple that fits to that location in the board matrix"""
    # Checks if the first value of the string is alphabetic
    if name[0].isalpha() == False:
        return None
    else:
        # If yes checks the last of the input can be cast to int
        for i in range(1,len(name)):
            if helper.is_int(name[i]) == False:
                return None
    column = name[0].upper()
    row = name[1:]
    row = int(name[1:]) - 1
    column = (ord(column) % 65)
    if check_row_col(row,column) == False:
        return None
    return row, column

def valid_ship(board, size, loc):
    """This function gets a board size of a ship and a location indicates
    the start of the ship and return if its possible to put it in the board"""
    row = loc[0]
    col = loc[1]
    if row + size > helper.NUM_ROWS:
        return False
    for i in range(size):
        if board[row + i][col] == helper.SHIP:
            return False
    return True

def create_player_board(rows = helper.NUM_ROWS, \
    columns = helper.NUM_COLUMNS, ship_sizes = helper.SHIP_SIZES):
    """This function sets submrines in specifics sides in location the user 
    choose, if location is not valid the function will ask for another one"""
    board = init_board(rows, columns) # Initializing an empty board 
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
                print("Invalid location")
                continue
            if valid_ship(board,size, loc) == False:
                print("Invalid location")
                continue
            for i in range(size):
                board[loc[0] + i][loc[1]] = helper.SHIP
            break
    helper.print_board(board)
    return board

def check_avalibale_spots(board):
    """This function gets the player board and return a list of tuples, 
    each tuple represent avalibalse spot"""
    lst = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == helper.WATER:
                loc = (i, j)
                lst.append(loc)
    return lst

def  create_computer_board(player_board, rows = helper.NUM_ROWS, \
    columns = helper.NUM_COLUMNS, ship_sizes = helper.SHIP_SIZES):
    """This function gets the player board and chhose a place to put 
    submarines"""
    free_spots = check_avalibale_spots(player_board)
    board = init_board(rows, columns)
    # Going over the tuple of ship sizes
    for size in ship_sizes:
        # Checking to choose again while the location does not fit to the
        # ship size
        while True:
            cell = helper.choose_ship_location(board, size, free_spots)
            row = cell[0]
            col = cell[1]
            if valid_ship(player_board, size, cell) == False:
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
    if board[row][col] == helper.SHIP:
        i = 0
        while board[row + i][col] == helper.SHIP:
                board[row+ i ][col] = helper.HIT_SHIP
                i += 1
    else:
        board[row][col] = helper.HIT_WATER
    return board
    
def main():
    player_board = create_player_board()
    lst = check_avalibale_spots(player_board)
    computer_board = create_computer_board(player_board)
    helper.print_board(player_board, computer_board)
    for item in lst:
        if player_board[item[0]][item[1]] == helper.SHIP:
            print("false")
            

if __name__ == "__main__":
    main()
    