liste = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

max_value = liste[0]

for number in liste:
    if max_value < number: 
        max_value = number
        
print(max_value)