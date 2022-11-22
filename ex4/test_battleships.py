import battleship
import helper


def test_init_board():
    board = battleship.init_board(rows=5, columns=3)
    assert len(board) == 5
    assert len(board[0]) == 3
    for i in board:
        for j in i:
            assert j == 0
    board = battleship.init_board(rows=0, columns=0)
    assert len(board) == 0


def test_check_row_col():
    board = battleship.init_board(99, 26)
    assert battleship.check_row_col(98, 25, board) == True


def test_cell_loc():
    assert battleship.cell_loc("a1") == (0, 0)
    assert battleship.cell_loc("a1") == (0, 0)
    assert battleship.cell_loc("a0") == (-1, 0)
    assert battleship.cell_loc("A1") == (0, 0)
    assert battleship.cell_loc("b1") == (0, 1)
    assert battleship.cell_loc("1A") == None
    assert battleship.cell_loc("-12a") == None
    assert battleship.cell_loc("99SA") == None
    assert battleship.cell_loc("Z99") == (98, 25)
    assert battleship.cell_loc("00") == None


def test_check_avalibale_spots():
    board = battleship.init_board(2, 2)
    dots = battleship.check_avalibale_spots(board, 0)
    assert dots == {(0, 0), (0, 1), (1, 0), (1, 1)}
    dots = battleship.check_avalibale_spots(board, 2)
    assert dots == {(0, 0), (0, 1)}
    dots = battleship.check_avalibale_spots(board, 3)
    assert dots == set()


def test_valid_ship():
    board = battleship.init_board(10, 10)
    size = 10, 5, 4
    board[4][6] = helper.SHIP
    assert battleship.valid_ship(board, size[0], (1, 1)) == False
    assert battleship.valid_ship(board, size[0], (0, 0)) == True
    assert battleship.valid_ship(board, size[1], (6, 1)) == False
    assert battleship.valid_ship(board, size[1], (5, 0)) == True
    assert battleship.valid_ship(board, size[2], (4, 6)) == False
