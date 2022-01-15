import random

playerScore = 0
computerScore = 0
gameRounds = input("How many rounds would you like to play?")
roundsPlayed = 0
computerOptions = ["Rock", "Paper", "Scissors"]


while gameRounds != "":
    if(gameRounds.isnumeric()):
        while roundsPlayed < int(gameRounds):
            playerChoice = input("Rock, Paper or Scissors?")
            print("You chose " + playerChoice)
            randomNumber = random.randrange(3)
            computerChoice = computerOptions[randomNumber]
            print("Computer chose " + computerChoice)
            if(playerChoice == "Rock" and computerChoice == "Scissors" or
                    playerChoice == "Scissors" and computerChoice == "Paper" or
                    playerChoice == "Paper" and computerChoice == "Rock" ):
                playerScore += 1
                roundsPlayed +=1
                print("you scored a point")
                print("The current score is player " + str(playerScore) + " computer " + str(computerScore))
            elif (playerChoice == "Rock" and computerChoice == "Paper" or
                    playerChoice == "Paper" and computerChoice == "Scissors" or
                    playerChoice == "Scissors" and computerChoice == "Rock"):
                computerScore +=1
                roundsPlayed += 1
                print("The computer scored a point")
                print("The current score is player " + str(playerScore) + " computer " + str(computerScore))
            elif (playerChoice == "Rock" and computerChoice == "Rock" or
                  playerChoice == "Scissors" and computerChoice == "Scissors" or
                  playerChoice == "Paper" and computerChoice == "Paper"):
                roundsPlayed += 1
                print("Draw! Nobody scored a point")
                print("The current score is player " + str(playerScore) + " computer " + str(computerScore))
            else:
                print("Error: Please try again")
        if(int(gameRounds) == roundsPlayed):
            if (playerScore > computerScore):
                print("Congratulations! You won the game!")
                break
            elif (playerScore < computerScore):
                print("Better luck next time... Computer won the game")
                break
            else:
                print("Game ended on a tie")
                tieBreaker = input("Would you like to play a tie breaker? (enter yes or no)")
                if (tieBreaker == "yes"):
                    gameRounds = "1"
                    roundsPlayed = 0
                elif (tieBreaker == "no"):
                    break
                else:
                    print("Error: enter yes or no")
    else:
        print("Error: please enter a number or press enter to exit")
        gameRounds = input("How many rounds would you like to play?")
print("Goodbye!")