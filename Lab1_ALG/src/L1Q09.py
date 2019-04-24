import random
randNum = random.randint(1, 9)
while True:
    guess = int(input("Guess the number (1~9) "))
    if guess < randNum:
        print("Your guessed is too low.")
    elif guess > randNum:
        print("Your guessed is too high.")
    else:
        print("You've guessed it right!")
        break

# print(str(randNum))
