from itertools import islice

# also find occurence of a word inside another word

filename = input("Give me a filename: ")
str_to_find = input("Give me the string you want to search: ")
file_object = open(filename, "r")

lines_number = len(file_object.readlines())

file_object.seek(0)

def find_str(str, substr):
    len_str = len(str)
    if len_str < len(substr):
        return False
    index = 0
    for character in substr:
        if str[index] != character:
            return False
        index += 1
    return True


words_number = 0
for line in islice(file_object, lines_number):
    line_len = len(line)
    for i in range(line_len):
        if find_str(line[i-1:], str_to_find):
            words_number += 1

print(words_number)
file_object.close()