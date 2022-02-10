import random 

def main():
    random_number = random.randint(1, 10)
    for _ in range(3):
        user_number = input("Donne moi un nombre: ")
        if user_number == "Quitter":
            break
        int_user_number = int(user_number)
        if int_user_number > 10:
            raise ValueError("Ton nombre est trop élevé ! Choisi une valeur entre 0 et 10")
        elif int_user_number < 0:
            raise ValueError("Ton nombre est trop petit ! Choisi une valeur entre 0 et 10")
        elif random_number == int_user_number:
            print("Tu as deviné le bon nombre !")
            break
        elif int_user_number > random_number:
            print("Ton nombre est plus grand que le nombre aléatoire !")
        else:
            print("Ton nombre est plus petit que le nombre aléatoire !")





if __name__ == "__main__":
    main()