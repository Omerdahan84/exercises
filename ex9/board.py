class Board:
    """
    This class represent a parking lot for the game
    """

    def __init__(self):
        """
        A constructor for a Board object
        the rules of the board are known so every initialization  should return the same board
        """
        # Initialize the board as a 2D list with all cells set to None
        self.__board = [['_' for _ in range(7)] for _ in range(7)]
        self.__board[3].append('_')
        # Initialize a dictionary to store the cars on the board, with keys being the car names and values being the car objects
        self.__cars = {}
        # Set the goal location to (3, 7)
        self.__goal = (3, 7)

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # Initialize the string representation of the board
        board_str = ""
        # Iterate over the rows and columns of the board
        for i in range(7):
            for j in range(7):
                board_str += str(self.__board[i][j])
             # Add a newline character after each row
            if i == 3:
                if self.__board[i][7] == '_':
                    board_str += ' E\n'
                else:
                    board_str += f"{self.__board[i][7]}\n"
            else:
                board_str += " *\n"
            # Return the string representation of the board
        return board_str

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # Initialize a list to store the cell coordinates
        cell_coords = []
        # Iterate over the rows and columns of the board
        for i in range(7):
            for j in range(7):
                # Add the current cell coordinates to the list
                cell_coords.append((i, j))
        # Add the goal location to the list
        cell_coords.append(self.__goal)
        # Return the list of cell coordinates
        return cell_coords

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,move_key,description)
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        # implement your code and erase the "pass"
        # Initialize a list to store the legal moves
        legal_moves = []
        # Iterate over the cars on the board
        for name in self.__cars:
            car = self.__cars[name]
            # Get the legal moves for the current car
            car_moves = car.possible_moves()
            # Iterate over the legal moves for the current car
            for move in car_moves:
                # Add the current move to the list of legal moves, including the car name and description
                # Get the list of cells that need to be empty for the move to be legal
                req_cells = car.movement_requirements(move)
                # Check if all the required cells are empty
                for cell in req_cells:
                    row, col = cell
                    if cell == self.__goal:
                        legal_moves.append((car.get_name(), move, car_moves[move]))
                    if row >= 7 or col >= 7 or col < 0 or row < 0:
                        continue
                    elif self.cell_content(cell) != '_':
                        continue
                    else:
                        legal_moves.append((car.get_name(), move, car_moves[move]))
        # Return the list of legal moves
        return legal_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return self.__goal

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        row, col = coordinate
        return self.__board[row][col]

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        # checks if car name is valid and not exits already
        # Check if the car name is already in use
        coordinates = car.car_coordinates()
        car_length = car.get_length()
        car_location = car.get_location()
        car_orientation = car.get_orientation()
        if car.get_name() in self.__cars:
            return False
        # Check if the car can be placed at its starting position
        if not self.is_valid_position_add(coordinates, car_length, car_location, car_orientation):
            return False

        # If all checks pass, add the car to the board and dictionary
        self._add_car_to_board(car, coordinates)
        self.__cars[car.get_name()] = car
        return True

    def _add_car_to_board(self, car, coordinates):
        """
        helper function for add car method
        :param car: the car we add to the board
        :param coordinates: the coordinates that car takes
        :return: updated board if the values of the car
        """
        for coordinate in coordinates:
            row, col = coordinate
            self.__board[row][col] = car.get_name()

    def is_valid_position_add(self, coordinates, length, location, orientation):
        """

        :param length of a car, list of coordinates this car is going to need to take, and starting location:
        :return:if it's legal to add this car in specific position
        """
        # checks if the car can fit to the board
        car_row = location[0]
        car_col = location[1]
        # if orientation == 0:
        #     if car_row + length > 7 or car_col < 0 or car_row < 0:
        #         return False
        # if orientation == 1:
        #     if car_col + length > 7 or car_col < 0 or car_row < 0:
        #         return False
        # checks if all the needed coordinates are empty
        for coordinate in coordinates:
            # checks if every cooridnate is in the board
            row, col = coordinate
            if row  == 3 and col == 7:
                continue
            if col >= 7 or row >= 7 or col < 0 or row < 0:
                return False
            if self.__board[row][col] != '_':
                return False
        # if all conditions satisfied return true
        return True

    def is_valid_position_move(self,requests, length, location, orientation):
        """
        :param length of a car, list of coordinates this car is going to need to take, and starting location:
        :return:if it's legal to add this car in specific position
        """
        # checks if the car can fit to the board
        car_row = location[0]
        car_col = location[1]
        if orientation == 0:
            if car_row + length > 7 or car_col < 0 or car_row < 0:
                return False
        if orientation == 1:
            if car_col + length > 7 or car_col < 0 or car_row < 0:
                return False
        for request in requests:
            # checks if every cooridnate is in the board
            row, col = request
            if row  == 3 and col == 7:
                continue
            if col >= 7 or row >= 7 or col < 0 or row < 0:
                return False
            if self.__board[row][col] != '_':
                return False
        return True

    def move_car(self, name, move_key):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param move_key: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        if name not in self.__cars:
            return False
        # Get the car object with the given name
        car = self.__cars[name]
        # Check if the given move is legal for the car
        found_key = False
        for move in self.possible_moves():
            if move_key in move and move[0] == name:
                found_key = True
                break
        if not found_key:
            return False
        # Get the list of cells that need to be empty for the move to be legal
        req_cells = car.movement_requirements(move_key)
        # Check if all the required cells are empty
        car_length = car.get_length()
        car_location = car.get_location()
        car_orientation = car.get_orientation()

        # checks if location is valid
        if not self.is_valid_position_move(req_cells,car_length, car_location, car_orientation):
            return False
        self.pop(car.get_name(),car.car_coordinates())
        car.move(move_key)
        self.add_car(car)
        # Return True to indicate that the move was successful
        return True

    def pop(self,name,coordinates):
        """pop the car so we can move it"""
        for coordinate in coordinates:
            row,col = coordinate
            self.__board[row][col] = '_'
        self.__cars.pop(name)

    def get_cars(self):
        """
        :return:the dictinary of cars on the board
        """
        return self.__cars
