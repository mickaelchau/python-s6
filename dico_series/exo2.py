dico = {
     'Colorado' : 1,
     'Boston'   : "hkgb",
     'Minnesota': 10,
     'Milwaukee': "hk",
     'Seattle'  : 20
}

max_value = None

for key in dico:
    if type(dico[key]) == int:
        if max_value == None:
            max_value = dico[key]
        elif dico[key] > max_value:
            max_value = dico[key]

print(max_value)