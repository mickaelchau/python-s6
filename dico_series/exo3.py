user_value = input("value to find in Dictionary: ")


dico = {
     'Colorado' : 1,
     'Boston'   : "hkgb",
     'Minnesota': 10,
     'Milwaukee': "hk",
     'Seattle'  : 20
}
def is_in_dico(dico, value):
    for key in dico:
        if dico[key] == value:
            return True
    return False

print(is_in_dico(dico, user_value))