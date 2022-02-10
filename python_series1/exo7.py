interval = list(range(3000, 3750))
print(interval)

result = []

for number in interval:
    if number % 5 == 0 and number % 7 == 0:
        result.append(number)  

print(result)