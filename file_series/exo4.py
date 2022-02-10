from io import TextIOWrapper

filename = input("Give me a valid filename: ")
file_object = open(filename, "r+")
print(file_object.read())
file_object.truncate(0) # Transforme la taille du fichier en 0 bits
file_object.close()
