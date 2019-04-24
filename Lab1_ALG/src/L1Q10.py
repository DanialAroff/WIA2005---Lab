userNumber = int(input("Enter a number : "))
if userNumber > 1:
    for i in range(2, userNumber):
        if userNumber%i == 0:
            print("\n" + str(userNumber) + " is not a prime number.")
            print(i, "times", userNumber // i, "is", userNumber)
            break
    else:
        print("\n", userNumber, "is a prime number.")
else:
    print("\n", userNumber, "is not a prime number.")