from typing import List


class Car:
    """
    A class representing a car in rush hour game.
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        #sets value name
        self.__name = name
        #sets car length
        self.__length = length
        #sest car orientation
        self.__orientation = orientation
        #sets car location
        self.__location = location

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        row, col = self.__location
        if self.__orientation == 0:
            return [(row + i, col) for i in range(self.__length)]
        else:
            return [(row, col + i) for i in range(self.__length)]

    def get_orientation(self):
        return self.__orientation

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        # implement your code and erase the "pass"
        if self.__orientation == 0:
            return {'u': "This move make the car go one coordinate up", 'd': "This move make the car go one coordinate \
            down"}
        if self.__orientation == 1:
            return {'r': "This move make the car go one coordinate right", 'l': "This move make the car go one "
                                                                                "coordinate left"}

    def movement_requirements(self, move_key) -> List[tuple]:
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        row, col = self.__location
        if move_key == 'u':
            return [(row - 1, col)]
        elif move_key == 'd':
            return [(row + self.__length, col)]
        elif move_key == 'l':
            return [(row, col - 1)]
        elif move_key == 'r':
            return [(row, col + self.__length)]

    def move(self, move_key) -> bool:
        """ 
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        row, col = self.__location
        possible_moves = Car.possible_moves(self)
        if move_key in possible_moves:
            if move_key == 'u':
                self.__location = (row - 1, col)
            elif move_key == 'd':
                self.__location = (row + 1, col)
            elif move_key == 'l':
                self.__location = (row, col - 1)
            elif move_key == 'r':
                self.__location = (row, col + 1)
            return True
        return False
    def get_length(self):
        """
        :return: the length of a car
        """
        return self.__length
    def get_location(self):
        """

        :return: return the location of the car
        """
        return self.__location

    def get_name(self) -> str:
        """
        :return: The name of this car.
        """
        return self.__name