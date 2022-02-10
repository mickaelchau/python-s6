input1 = input("Donne moi une année: ")
year = int(input1)

if (year % 400 == 0):
    print(year, "est une année bissextile")
elif (year % 100 == 0):
    print(year, "n'est pas une année bissextile")
elif (year % 4 == 0):
    print(year, "est une année bissextile")
else:
    print(year, "n'est pas une année bissextile")
