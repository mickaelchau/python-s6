values = [1, 2, 3, 5, 9]
keys = ["micka", "robert", "clarel", "clara", "fanny" ]
dic_res = {}

len_list = len(keys)

for index in range(len_list):
    dic_res[keys[index]] = values[index]

print(dic_res)