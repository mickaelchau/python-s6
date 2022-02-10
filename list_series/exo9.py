liste1 = [1, 2, 3, 5, 9]
liste2 = [1, 1, 8, 78, 9 ]

def find_element(liste, element):
    liste_len = len(liste)
    for index in range(liste_len):
        if liste[index] == element:
            return True
    return False
liste1.sort()
liste2.sort()

last_element = liste1[0]

if find_element(liste2, last_element):
    print(last_element,end = " ")

len_liste1 = len(liste1)

for index1 in range (1, len_liste1):
    if last_element == liste1[index1]:
        continue
    if find_element(liste2, liste1[index1]):
        print(liste1[index1], end = " ")
    last_element = liste1[index1]


