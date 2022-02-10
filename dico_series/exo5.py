dico = {
    'Seattle'  : 20,
    'Colorado' : 1,
    'Boston'   : 5,
    'Minnesota': 10,
    'Milwaukee': 2,

}

print(sorted(dico.items(), key=lambda x:x[1], reverse=True))