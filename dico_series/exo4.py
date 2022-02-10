dico = {
    20: 'Seattle', 
    1: 'Colorado',
    5: 'Boston',
    10:'Minnesota',
    2: 'Milwaukee',
}
print(sorted(dico.items(), key=lambda x:x[0]))