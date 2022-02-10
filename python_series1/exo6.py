

voyels = ["a", "e", "i", "o", "u", "y"]
text = "Mickael"

def is_in_list(list, value):
    for element in list:
        if element == value:
            return 1
    return 0

voyels_count = 0
for character in text:
    is_voyel = is_in_list(voyels, character)
    voyels_count += is_voyel
    
print("Le nombre de voyelle est:", voyels_count)