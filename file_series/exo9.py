from itertools import islice

filename = input("Give me a filename: ")
file_object = open(filename, "r")

lines_number = len(file_object.readlines())

file_object.seek(0)

words_number = 0
for line in islice(file_object, lines_number):
    for character in line:
        if character == " " or character == "'":
            words_number += 1 
    words_number + 1

print(words_number)
file_object.close()