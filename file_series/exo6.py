files_to_merge = ["file1.txt", "file2.txt", "file3.txt"]
result_file = "demofile.txt"

result_file_object = open(result_file, "w")

for filename in files_to_merge:
    print(filename)
    file_object = open(filename, "r")
    result_file_object.write(file_object.read() + "\n")
    file_object.close()

    
result_file_object.close()