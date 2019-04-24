a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# dumb way
# for i in range(0,len(a),1):
#     if a[i]%2 == 0:
#         print(str(a[i]),end=" ")

b = [i for i in a if i % 2 == 0]
print(b)
