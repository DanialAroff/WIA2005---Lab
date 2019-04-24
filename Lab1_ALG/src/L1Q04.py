userNo = int(input("Enter a number "))

print("Divisor of number " + str(userNo) + "\n")
for i in range(1, userNo + 1):
    if userNo % i == 0:
        print(str(i), end=" ")
        i += 1
    else:
        i += 1
