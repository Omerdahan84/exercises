import helper


def init_board(rows = helper.NUM_ROWS, columns = helper.NUM_COLUMNS):
    """This function intialzaing an empty board"""
    # Using list comprehension to create a list with the sign for empty cell
    # this list will pass as a paramer to a list comprehension to create
    # a matrix
    board = [[helper.WATER for i in range(columns)] for j in range(rows)]
    return board


def cell_loc(name):
    column = making_upper(name)
    row = int(name[1:]) - 1
    column = (ord(column) % 65)
    if check_row_col(row,column) == False:
        return None
    return row, column

def check_row_col(row, col):
    if row >= len(board) or col >= len(board[0]):
        return False
    else:
        return True
def making_upper(name):
    return name[0].upper()


def valid_ship(board, size, loc):
    pass


def create_player_board(rows, columns, ship_sizes):
    pass


def fire_torpedo(board, loc):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
