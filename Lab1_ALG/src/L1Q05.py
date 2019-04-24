a = [1, 1, 2, 5, 7, 9, 11, 15]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in range(0, len(a)):
    if a[i] in b and a[i] not in c:
        c.append(a[i])
        i += 1

print('First list : ' + str(a))
print('Second list : ' + str(b))
print('Intersection of the 2 list : ' + str(c))
