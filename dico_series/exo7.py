user_input = input("Donne moi un entier: ")
user_input_value = int(user_input) 

dic_res = {}

for index in range(user_input_value):
    dic_res[index] = index*index

print(dic_res)
