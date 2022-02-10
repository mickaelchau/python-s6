Liste = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

user_limit = input("Donne moi l'entier maximum que je dois retourner: ")
user_limit_int = int(user_limit)

for number in Liste:
    if number <= 13: 
        print(number, end = " ")