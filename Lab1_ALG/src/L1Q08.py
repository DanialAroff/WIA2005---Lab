firstplayer = input("Enter Player 1 name : ")
secondplayer = input("Enter Player 2 name : ")

while True:
    player1 = input(firstplayer + " - ")
    player2 = input(secondplayer + " - ")
    if (player1 == 'paper' and player2 == 'rock'):
        print(firstplayer + " wins!!")
    elif (player1 == 'paper' and player2 == 'scissor'):
        print(secondplayer + " wins!!")
    elif (player1 == 'rock' and player2 == 'scissor'):
        print(firstplayer + " wins!!")
    elif (player1 == 'rock' and player2 == 'paper'):
        print(secondplayer + " wins!!")
    elif (player1 == 'scissor' and player2 == 'paper'):
        print(firstplayer + " wins!!")
    elif (player1 == 'scissor' and player2 == 'rock'):
        print(secondplayer + " wins!!")
    else:
        print("It's a draw!")
    cont = input("\nContinue playing? Y/N")
    if cont == 'N':
        break
    else:
        print("Continue")
