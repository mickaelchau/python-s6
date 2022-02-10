nom = input("Quel est ton nom ? ")
age = input("Quel est ton âge ? ")
age_int = int(age)
years_before_100 = 100 - age_int
current_year = 2022

print(nom, "aura 100 ans en", current_year + years_before_100)
