from typing import List, Tuple, Set, Optional


# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    this function return the max numbers of cells can be seen from a cell in
    a partial picture
    param: picture: Picture, row: int, col: int
    return: integer
    """
    count = 0
    #if the cell is black so no cell can be seen
    if picture[row][col] == 0:
        return  0
    #checking the cells in the same column
    #every loop check the sides of the cell where the first loop also count the cell itself.
    #we're counting along the row/col if we see a black cell we can't see afterwards, so we break the loop
    for i in range(row,-1,-1):
        if picture[i][col] == 0:
            break
        else:
            count+=1
    for i in range(row+1,len(picture),1):
        if picture[i][col] == 0:
            break
        else:
            count+=1
    for i in range(col-1,-1,-1):
        if picture[row][i] == 0:
            break
        else:
            count+=1
    for i in range(col+1, len(picture[0]), 1):
        if picture[row][i] == 0:
            break
        else:
            count+=1
    return count


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
        this function return the max numbers of cells can be seen from a cell in
        a partial picture
        param: picture: Picture, row: int, col: int
        return: integer
        """
    count = 0
    # if the cell is black so no cell can be seen
    if picture[row][col] == 0 or picture[row][col] == -1:
        return 0
    # checking the cells in the same column
    # every loop check the sides of the cell where the first loop also count the cell itself.
    # we're counting along the row/col if we see a black cell we can't see afterwards, so we break the loop
    for i in range(row, -1, -1):
        if picture[i][col] == 0 or picture[i][col] == -1:
            break
        else:
            count += 1
    for i in range(row + 1, len(picture), 1):
        if picture[i][col] == 0 or picture[i][col] == -1:
            break
        else:
            count += 1
    for i in range(col - 1, -1, -1):
        if picture[row][i] == 0 or picture[row][i] == -1:
            break
        else:
            count += 1
    for i in range(col + 1, len(picture[0]), 1):
        if picture[row][i] == 0 or picture[row][i] == -1 :
            break
        else:
            count += 1
    return count


def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    for constraint in constraints_set:
        row,col,seen = constraint
        max_seen = max_seen_cells(picture,row,col)
        min_seen = min_seen_cells(picture,row,col)
        if seen < min_seen or seen > max_seen:
            return 0
        if max_seen != min_seen and min_seen <= seen <= max_seen:
            return 2
    return 1



def grid_builder(n:int,m:int) -> Picture:
    """get a dimensions of a grid and return an empty grid
    param: m-number of rows,n number of columns
    return: grid"""
    return [[-1 for _ in range(m)] for _ in range(n)]


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    """return a solution for a board with set of constraints, if there is no solution return None"""
    grid = grid_builder(n,m)
    # Start the backtracking search.
    return solve_puzzle_helper(0, 0,constraints_set,n,m,grid)
def solve_puzzle_helper(row: int, col: int,constraints_set: Set[Constraint], n: int, m: int,grid:Picture) -> Optional[Picture]:
    # If we have reached the last cell, we have found a valid solution.
    if row == n-1 and col == m:
        return grid

    # If we have reached the end of a row...
    if col == m:
        row += 1
        col = 0

    # Skip cells that already have a value.
    if grid[row][col] != -1:
        return solve_puzzle_helper(row, col + 1,constraints_set,n,m,grid)

    # Try setting the current cell to 0.

    for value in (0,1):
        grid[row][col] = value
        if check_constraints(grid, constraints_set) != 0 :
            solution = solve_puzzle_helper(row, col + 1,constraints_set,n,m,grid)
            if solution is not None:
                return solution

        # If none of the above worked, backtrack.
    grid[row][col] = -1
    return None


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    grid = grid_builder(n,m)
    # Start the backtracking search.
    return how_many_helper(0, 0, constraints_set, n, m, grid)
def how_many_helper(row: int, col: int,constraints_set: Set[Constraint], n: int, m: int,grid:Picture,) -> Optional[Picture]:

    # If we have reached the last cell, we have found a valid solution.
    if row == n-1 and col == m:
        return 1
    # If we have reached the end of a row...
    if col == m:
        row += 1
        col = 0

    # Skip cells that already have a value.
    if grid[row][col] != -1:
        return how_many_helper(row, col + 1,constraints_set,n,m,grid)

    # Try setting the current cell to 0.
    count = 0
    for value in (0,1):
        grid[row][col] = value
        if check_constraints(grid, constraints_set) != 0 :
            count += how_many_helper(row, col + 1,constraints_set,n,m,grid)


     # If none of the above worked, backtrack.
    grid[row][col] = -1
    return count

def generate_puzzle(picture: Picture) -> Set[Constraint]:
    ...
