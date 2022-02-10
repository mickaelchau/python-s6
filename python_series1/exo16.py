user_value = input("Donne moi un entier: ")
int_user_value = int(user_value)
#interval = list(range(1, 50))

def is_prime(number):
    if (number < 2):
        return False
    index = int(number/2)
    is_divisible = False
    while (not(is_divisible) and index >= 2):
        if number % index == 0:
            is_divisible = True
        index -= 1
    return not(is_divisible)

print(is_prime(int_user_value))
"""
for i in range(50):
    print(i, is_prime(i))
"""