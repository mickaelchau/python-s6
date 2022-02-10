class Message():
    information_message = ""
    error_message = ""
    def __init__(self, information_message, error_message):
        self.information_message = information_message
        self.error_message = error_message

class Functions():
    function = None
    verification_function = None
    def __init__(self, function, verification_messsage):
        self.function = function
        self.verification_function = verification_messsage

def get_user_input(messages, functions):
    user_input = functions.function(messages.information_message)
    while (not(functions.verification_function(user_input))):
        print(messages.error_message)
        user_input = functions.function(messages.information_message)
    return user_input