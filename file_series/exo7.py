from itertools import islice

filename = input("Give me a filename: ")
file_object = open(filename, "r")

lines_number = len(file_object.readlines())

file_object.seek(0)

for line in islice(file_object, lines_number):
    print(line, end = "")

file_object.close()