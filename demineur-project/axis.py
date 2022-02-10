from input import Functions, Message, get_user_input

class Axis():
    values = None
    name = ""

    def __init__(self, name, values):
        self.values = values
        self.name = name

    def is_in_axis(self, value):
        value_ascii = ord(value)
        if value_ascii < ord(self.values[0]) or value_ascii > ord(self.values[len(self.values) - 1]):
            return False
        return True

    def get_start(self):
        return self.values[0]
    
    def get_end(self):
        return self.values[len(self.values) - 1]

    def get_index(self, coordonate):
        return ord(coordonate) - ord(self.values[0])    
    
class Point():
    x = None
    y = None
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
        
lines_axis = Axis("x", [chr((ord('A') + i)) for i in range(10)])
columns_axis = Axis("y", [chr(i + ord('0')) for i in range(10)])


def format_get_in_axis_value_message(axis):
    get_value_message = "Choisi une coordonée {coordinate} entre {start} et {end}: "
    return get_value_message.format(
        coordinate = axis.name, 
        start = axis.get_start(), 
        end = axis.get_end()
    )
    
invalid_get_in_axis_value_message = "Ce n'est pas une coordonnée valide"

def get_in_axis_value(axis):
    get_in_axis_value_message = format_get_in_axis_value_message(axis)
    get_user_level_messages = Message(get_in_axis_value_message, invalid_get_in_axis_value_message)
    get_user_level_functions = Functions(input, axis.is_in_axis)
    axis_value = get_user_input(get_user_level_messages, get_user_level_functions)
    return axis_value

def get_user_point(message):
    print(message)
    line_value = get_in_axis_value(lines_axis)
    column_value = get_in_axis_value(columns_axis)

    board_x = lines_axis.get_index(line_value)
    board_y = columns_axis.get_index(column_value)

    point = Point(board_x, board_y)
    return point
