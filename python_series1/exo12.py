def range_of_charcaters_from_ascii(start, end):
    interval = list(range(start, end + 1))
    map_interval = map(chr, interval)
    characters = list(map_interval)
    return characters

def is_value_in_list(list, value):
    for element in list:
        if element == value:
            return True
    return False

def is_one_char_of_str_in_list(list, str):
    is_char_in_list = False
    for character in str:
        if is_value_in_list(list, character):
            is_char_in_list = True
    return is_char_in_list

lowercase_characters = range_of_charcaters_from_ascii(97, 122)
uppercase_characters = range_of_charcaters_from_ascii(65, 90)
special_characters = ['@', '&', '$', '#']

while True:
    password = input("Veuillez entrer un mot de passe valide: ")
    length = len(password)
    if length < 6 or length > 12:
        continue
    has_lowercase = is_one_char_of_str_in_list(lowercase_characters, password)
    if not(has_lowercase):
        continue
    has_uppercase = is_one_char_of_str_in_list(uppercase_characters, password)
    if not(has_uppercase):
        continue
    has_special = is_one_char_of_str_in_list(special_characters, password)
    if not(has_special):
        continue
    break 
