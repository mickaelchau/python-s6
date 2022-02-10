from operator import pos

possible_gestures = [ "Pierre", "Papier", "Ciseau"]

class Player:
    id = 0
    pseudo = ""
    gesture = ""
    get_pseudo_message = ""
    get_gesture_message = ""
    win_message = ""

    def __init__(self, id):
        self.get_pseudo_message = "Player with the id " + str(id) + ", choose your pseudo: "
        self.id = id

    def get_pseudo(self):
        self.pseudo = input(self.get_pseudo_message) 
        self.win_message = self.pseudo + " wins !"

    def get_gesture(self):
        self.get_gesture_message = self.pseudo + ", choose your gesture: "
        while (not(is_valid_gesture(self.gesture))):
            self.gesture = input(self.get_gesture_message)
    
    def print_win(self):
        print(self.pseudo, "wins !")



def is_value_in_list(list, value):
    for element in list:
        if element == value:
            return True
    return False

def is_valid_gesture(str):
    if is_value_in_list(possible_gestures, str) == True:
        return True
    return False

def get_gesture(pseudo):
    gesture = ""
    while (not(is_valid_gesture(gesture))):
        gesture = input(pseudo, "Choisissez entre Pierre, Feuille et Ciseau")
    return gesture

def who_wins(player1, player2):
    if player1.gesture == player2.gesture:
        print("Egalité entre les 2 joueurs !")
    if player1.gesture == "Pierre":
        if player2.gesture == "Ciseaux":
            player1.print_win()
        else:
            player2.print_win()
    if player1.gesture == "Ciseaux":
        if player2.gesture == "Papier":
            player1.print_win()
        else:
            player2.print_win()
    if player1.gesture == "Papier":
        if player2.gesture == "Pierre":
            player1.print_win()
        else:
            player2.print_win()


def main():
    player1 = Player(1)
    player2 = Player(2)
    player1.get_pseudo()
    player1.get_gesture()
    player2.get_pseudo()
    player2.get_gesture()
    who_wins(player1, player2)
    
if __name__ ==  "__main__":
    main()
