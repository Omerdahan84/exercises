from car import *
from board import *
from game import *
import sys


class Car1(Car):
    def move(self, move_key):
        Car.move(self, move_key)
        self.__dict__[location] = (5, 1)
        return True


class Car2(Car):
    def movement_requirements(self, move_key):
        return [(2, 0), (7, 0)]


class Car3(Car):
    def car_coordinates(self):
        return [(5, 0), (7, 0), (6, 0)]


class Car4(Car):
    def possible_moves(self):
        return {"aa": ""}

    def movement_requirements(self, move_key):
        return [(1, 3)]


class Board1(Board):
    def target_location(self):
        return 5, 5


def get_loc_attr():
    carr = Car("R", 2, (0, 0), 0)

    before = set(carr.__dict__.items())
    carr.move('d')
    after = set(carr.__dict__.items())
    return (before - after).pop()[0] if before - after else None


def test_move_req():
    _car = Car2("R", 2, (0, 0), 0)
    b = Board()
    b.add_car(_car)
    assert not b.move_car("R", "d")


def test_coords():
    _car = Car3("R", 3, (0, 0), 0)
    b = Board()
    assert not b.add_car(_car)


def test_possible_moves():
    _car = Car4("R", 2, (1, 1), 0)
    car1 = Car4("O", 7, (6, 0), 1)
    b = Board()
    b.add_car(_car)
    b.add_car(car1)
    assert len(b.possible_moves()) == 2
    assert all(m[1] == "aa" for m in b.possible_moves())


def test_target():
    def input(*args):
        assert False

    sys.modules["builtins"].input = input
    b = Board1()
    _game = Game(b)
    b.add_car(Car("R", 3, (5, 3), 1))
    _game.play()


def test_move_car():
    assert location
    if location:
        _car = Car1("R", 2, (0, 0), 0)
        b = Board()
        b.add_car(_car)
        b.move_car("R", "d")
        assert b.cell_content((5, 1))


location = get_loc_attr()
