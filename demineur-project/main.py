import level
import board
import axis
from input import Functions, Message, get_user_input

welcome_message = "Bienvenue dans le jeu du Démineur !\nE: Empty\nM: Mined\nX: Hidden Cell\n" 
invalid_get_user_point_message = "Cette case est déjà visible. Choisis en une autre"
get_user_point_message = "Saisi une case:"

def get_user_point():
    get_user_point_messages = Message(get_user_point_message, invalid_get_user_point_message)
    get_user_point_functions = Functions(axis.get_user_point, board.is_valid_cell)
    point = get_user_input(get_user_point_messages, get_user_point_functions)
    return point

def init_game():
    print(welcome_message)
    chosen_level = level.get_user_level()
    mines_bumber = level.get_mines_number(chosen_level)
    board.inject_board_mines(mines_bumber)
    board.print_board()

def play_game():
    continue_playing = True 
    while continue_playing:
        point = get_user_point()
        board.discover_cell(point)
        board.print_board()
        if board.is_lost(point):
            continue_playing = False

def count_points():
    return board.count_visible_and_empty_cells()

def end_game():
    points = count_points()
    print("Bravo ! Tu as marqué {points}".format(points = points))

def main():
    init_game()
    play_game()
    end_game()

if __name__ == "__main__":
    main()