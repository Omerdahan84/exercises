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
        if picture[i][col] == 0 or picture[row][i] == -1:
            break
        else:
            count += 1
    for i in range(row + 1, len(picture), 1):
        if picture[i][col] == 0 or picture[row][i] == -1:
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
        if seen != min_seen and seen != max_seen and (min_seen > seen or seen > max_seen):
            return 0
        if max_seen != min_seen and min_seen <= seen <= max_seen:
            return 2
    return 1




def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    """"""
    grid = [[-1 for _ in range(m)] for _ in range(n)]

    def backtrack(row: int, col: int) -> Optional[Picture]:
        # If we have reached the last cell, we have found a valid solution.
        if row == n and col == m:
            return grid

        # If we have reached the end of a row, move to the next row.
        if col == m:
            row += 1
            col = 0

        # Skip cells that are part of a constraint.
        if (row, col) in constraints_set:
            return backtrack(row, col + 1)

        # Try filling the current cell with a 0 or a 1.
        for value in (0, 1):
            grid[row][col] = value

            # Check if the constraints are satisfied.
            if check_constraints(grid, constraints_set) == 1 or check_constraints(grid, constraints_set) == 2:
                # If the constraints are satisfied, continue searching for a solution.
                result = backtrack(row, col + 1)
                if result is not None:
                    return result

            # If we reach this point, it means that we have tried filling the current
            # cell with both 0 and 1, but neither choice led to a valid solution.
            # This means that the previous choices we made were not valid, so we need
            # to backtrack (undo our choices) and try a different set of choices.
            grid[row][col] = 0
            return

    return backtrack(0, 0)

print( solve_puzzle({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3))
def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    ...


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    ...
