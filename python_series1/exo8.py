stars = 1

def stars_line(number):
    while (number > 0):
        print('*', end ='')
        number -= 1
    print()

while (stars <= 6):
    stars_line(stars)
    stars += 1

stars -= 2

while (stars >= 1):
    stars_line(stars)
    stars -= 1