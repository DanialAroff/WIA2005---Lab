a = [1, 1, 2, 3, 4, 4, 5, 7, 12, 30, 49]

for i in range(0, len(a)):
    if a[i] < 5:
        print(str(a[i]) + " ")
        i += 1
    else:
        i += 1
