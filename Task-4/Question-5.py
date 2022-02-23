n = 5
sp = n - 1
for i in range(0, n):
    for j in range(0, sp):
        print(end = " ")
    sp = sp - 1
    for j in range(0, i + 1):
        print("*", end = " ")
    print()