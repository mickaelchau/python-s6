liste = [1, 1, 2, 3, 5, 8, 0, 21, 0, 55, 89, 0]

liste_len = len(liste)

for index in range(liste_len):
    if liste[index] == 0: 
        liste[index] = 5       
         
print(liste)