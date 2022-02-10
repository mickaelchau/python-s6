input1 = input("Donne moi un premier entier: ")
int_input1 = int(input1)

input2 = input("Donne moi un deuxième entier: ")
int_input2 = int(input2)

if (int_input1 % int_input2 == 0):
    print(int_input1, "est divisible par", int_input2)
else:
    print(int_input1, "n'est pas divisible par", int_input2)