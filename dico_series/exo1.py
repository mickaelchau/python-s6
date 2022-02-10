dico = {
     'Colorado' : 1,
     'Boston'   : "hkgb",
     'Minnesota': 10,
     'Milwaukee': "hk",
     'Seattle'  : 20
}

values_sum = 0

for key in dico:
    if type(dico[key]) == int:
        values_sum += dico[key]

print(values_sum)