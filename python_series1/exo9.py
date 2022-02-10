interval = list(range(1, 50))

for number in interval:
    divisible_by_3 = True if (number % 3 == 0) else False
    divisible_by_5 = True if (number % 5 == 0) else False 
    if divisible_by_3 and divisible_by_5:
        print("Multiple de Trois et de Cinq")
    elif divisible_by_5:
        print("Multiple de Cinq")
    elif divisible_by_3:
        print("Multiple de Trois")
    else:
        print(number)
