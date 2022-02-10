from_filename = input("Give me a filename that you want to copy the content: ")
to_filename = input("Give me the filename of the copy: ")

from_file_object = open(from_filename, "r")
to_file_object = open(to_filename, "w")

to_file_object.write(from_file_object.read())

from_file_object.close()
to_file_object.close()