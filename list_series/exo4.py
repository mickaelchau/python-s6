liste = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 0]

min_value = liste[0]

for number in liste:
    if min_value > number: 
        min_value = number
        
print(min_value)