import  helper
import sys
from board import *
from car import *

class Game:
    """
    this class represent the rush hour game
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param: board: An object of type board
        """
        self.__board = board
        self.__game_over = False


    def __single_turn(self):
        """
        Note - this function is here to guide you, and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        cars = self.__board.get_cars()#get the cars dict from the board
        goal = self.__board.target_location()#get the goal from the board
        # Get the user's input for the car name and move direction

        car_name,move_direction = input("Enter the name of the car you want to move,and the direction you would \
like to move it(name,direction,finish='!'): ").split(',')
        if car_name not in cars:
            print("Invalid car name. Please try again.")
        elif not self.__board.move_car(car_name,move_direction):
            print("this move is not allowed for this car")
            #if this moves winning the game,finish the game

    def is_win_car(self):
        """checks if thers is a car in the goal cell"""
        cars = self.__board.get_cars()
        goal = self.__board.target_location()
        for car_name in cars:
            if goal in cars[car_name].car_coordinates():
               return True
        return False
    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        #this block runs the game
        while not self.__game_over:
            #checks if there is a car in the goal cell
            if self.is_win_car():
                self.__game_over = True
                print(self.__board)
                print("you won,good game!")
                self.__game_over = True
                break
            print(self.__board)
            self.__single_turn()




def create_board_from_config(config_file):
    """
    creates a board from a json file
    :param config_file:
    :return: a new board
    """
    game_board = Board()
    for config in config_file:

        car_name = config
        car_length = config_file[config][0]
        car_location = tuple(config_file[config][1])
        car_orientation = config_file[config][2]
        if not valid_name(car_name) or not valid_length(car_length) or not valid_orientation(car_orientation):
            continue
        car = Car(car_name,car_length,car_location,car_orientation)
        if not game_board.add_car(car):
            continue
        game_board.add_car(car)
    return game_board

def valid_orientation(orientation):
    """checks if car orientation is valid"""
    if orientation!= 1 and orientation!=0:
        return False
    return True

def valid_length(length):
    """checks if car length is valid"""
    if 2 <= length <=4 :
        return True
    return False

def valid_name(name):
    """
    checks if a car name is valid
    :param name:
    :return:
    """
    if name not in 'YBOGWR'  :
        return False
    return True



if __name__== "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    # implement your code and erase the "pass"

    json_path = sys.argv[1]#puts the json path in a variable
    board_config = helper.load_json(json_path)#open the json file with the helper function

    # Create a new Board object with the configuration from the JSON file

    board = create_board_from_config(board_config)

    # Create a new Game object with the Board object
    game = Game(board)

    # Start the game
    game.play()
