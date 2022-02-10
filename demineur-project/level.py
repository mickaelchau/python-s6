from input import Functions, Message, get_user_input

levels = ["débutant", "medium", "difficile", "expert"]
get_level_message = "Choisissez la difficulté du jeu entre 'débutant', 'medium', 'difficile', 'expert': "
invalid_get_level_message = "Ce n'est pas une difficultée valide"

def is_value_in_list(list, value):
    for element in list:
        if element == value:
            return True
    return False
    
def is_valid_level(level):
    return is_value_in_list(levels, level)

def get_user_level():
    get_user_level_messages = Message(get_level_message, invalid_get_level_message)
    get_user_level_functions = Functions(input, is_valid_level)
    user_level = get_user_input(get_user_level_messages, get_user_level_functions)
    return user_level

def get_mines_number(level):
    levels_index = 0
    while(levels[levels_index] != level):
        levels_index += 1
    return levels_index * 5
