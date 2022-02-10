from logging import raiseExceptions
from math import sqrt

a = 2
b = 5
c = 1

racines = []

def find_racines(a, b, c):
    delta = b*b - 4*a*c
    if delta < 0:
       raise ValueError
    elif delta == 0:
        racines.append(-b/2*a)
    else:
        racines.append((-b + sqrt(delta)) / (2 * a))
        racines.append((-b - sqrt(delta)) / (2 * a))

find_racines(a, b, c)
print(racines)