def print_fibonacci_sequence(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0,f1 = 0, 1
    print(f0, f1, end=" ")
    index = 0 
    while (index < n):
        f0, f1 = f1, f1 + f0
        index += 1
        print(f1, end=" ")

print_fibonacci_sequence(50)
