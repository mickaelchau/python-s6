from enum import Enum
import random
from axis import lines_axis, columns_axis

class State(Enum):
    MINED = 0
    EMPTY = 1  

class Visibility(Enum):
    HIDDEN = 0
    VISIBLE = 1 

class Cell:
    visibility = Visibility.HIDDEN
    state = State.EMPTY

    def reveal(self):
        self.visibility = Visibility.VISIBLE

    def is_mined(self):
        if self.state == State.MINED:
            return True
        return False

    def is_empty(self):
        if self.state == State.EMPTY:
            return True
        return False

    def is_hidden(self):
        if self.visibility == Visibility.HIDDEN:
            return True
        return False

    def is_visible(self):
        if self.visibility == Visibility.VISIBLE:
            return True
        return False
        
    def mine(self):
        self.state = State.MINED

board = [[Cell() for _ in range(10)] for _ in range(10)]


def inject_board_mines(mines_number):
    for _ in range(mines_number):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        board[x][y].mine()

def state_representation(state): 
    if state == State.EMPTY:
        return 'E'
    else:
        return 'M'

def print_board():
    print("", end = "  ")
    for nth_column in columns_axis.values:
        print(nth_column, end = " ")
    print()
    board_len = len(board)
    for i in range(board_len):
        print(lines_axis.values[i], end = " ")
        for cell in board[i]:
            if cell.visibility == Visibility.VISIBLE:
                print(state_representation(cell.state), end = " ")
            else: 
                print("X", end = " ")
        print()


def is_valid_cell(point):
    return board[point.x][point.y].is_hidden()

def discover_cell(point):
    board[point.x][point.y].reveal()

def is_lost(point):
    return board[point.x][point.y].is_mined()

def count_visible_and_empty_cells():
    count = 0
    for line in board:
        for cell in line:
            if cell.is_visible() and cell.is_empty():
                count += 1

