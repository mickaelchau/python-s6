filename = input("Give me a filename: ")
file_object = open(filename, "r")

lines_number = len(file_object.readlines())
print(lines_number)

file_object.close()