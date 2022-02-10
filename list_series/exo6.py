str = "je suis a"
str_len = len(str)

character_to_find = 'b'

for index in range(str_len):
    if str[index] == character_to_find:
        print(index)
