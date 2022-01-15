import random

playerScore = 0
computerScore = 0
playerChoice = input("Rock, Paper or Scissors?")
computerOptions = ["Rock", "Paper", "Scissors"]

while playerScore < 3 and computerScore < 3:
    print(playerChoice)
    randomNumber = random.randrange(3)
    computerChoice = computerOptions[randomNumber]
    if(playerChoice == "Rock" and computerChoice == "Scissors" or
            playerChoice == "Scissors" and computerChoice == "Paper" or
            playerChoice == "Paper" and computerChoice == "Rock" ):
        playerScore += 1
        print("you scored a point")
        print("The current score is player " + str(playerScore) + " computer " + str(computerScore))
        if (playerScore == 3):
            print("Congratulations! You won the game!")
            break
        elif (computerScore == 3):
            print("Better luck next time... Computer won the game")
            break
    elif (playerChoice == "Rock" and computerChoice == "Paper" or
            playerChoice == "Paper" and computerChoice == "Scissors" or
            playerChoice == "Scissors" and computerChoice == "Rock"):
        computerScore +=1
        print("The computer scored a point")
        print("The current score is player " + str(playerScore) + " computer " + str(computerScore))
        if (playerScore == 3):
            print("Congratulations! You won the game!")
            break
        elif (computerScore == 3):
            print("Better luck next time... Computer won the game")
            break
    elif (playerChoice == "Rock" and computerChoice == "Rock" or
          playerChoice == "Scissors" and computerChoice == "Scissors" or
          playerChoice == "Paper" and computerChoice == "Paper"):
        print("Draw! Nobody scored a point")
        print("The current score is player " + str(playerScore) + " computer " + str(computerScore))
        if (playerScore == 3):
            print("Congratulations! You won the game!")
            break
        elif (computerScore == 3):
            print("Better luck next time... Computer won the game")
            break
    else:
        print("Error: Please try again")

    playerChoice = input("Rock, Paper or Scissors?")
    randomNumber = random.randrange(2)
    computerChoice = computerOptions[randomNumber]
