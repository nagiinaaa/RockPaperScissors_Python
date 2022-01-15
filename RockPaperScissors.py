import random

playerScore = 0
computerScore = 0
gameRounds = input("How many rounds would you like to play? (enter odd number)")
roundsPlayed = 0
computerOptions = ["Rock", "Paper", "Scissors"]


while gameRounds != "":
    if (not gameRounds.isnumeric()):
        print("Error: please enter an odd number or press enter to exit")
        gameRounds = input("How many rounds would you like to play? (enter odd number)")
    elif(int(gameRounds) % 2 != 0):
        playerChoice = input("Rock, Paper or Scissors?")
        print(playerChoice)
        randomNumber = random.randrange(3)
        computerChoice = computerOptions[randomNumber]
        while playerScore < int(gameRounds) and computerScore < int(gameRounds):
            if(playerChoice == "Rock" and computerChoice == "Scissors" or
                    playerChoice == "Scissors" and computerChoice == "Paper" or
                    playerChoice == "Paper" and computerChoice == "Rock" ):
                playerScore += 1
                roundsPlayed +=1
                print("you scored a point")
                print("The current score is player " + str(playerScore) + " computer " + str(computerScore))
                if(roundsPlayed == int(gameRounds)):
                    if(playerScore > computerScore):
                        print("Congratulations! You won the game!")
                        gameRounds=""
                        break
                    elif(playerScore < computerScore):
                        print("Better luck next time... Computer won the game")
                        gameRounds=""
                        break
                    else:
                        print("Game ended on a tie")
                        gameRounds = ""
                        break
            elif (playerChoice == "Rock" and computerChoice == "Paper" or
                    playerChoice == "Paper" and computerChoice == "Scissors" or
                    playerChoice == "Scissors" and computerChoice == "Rock"):
                computerScore +=1
                roundsPlayed += 1
                print("The computer scored a point")
                print("The current score is player " + str(playerScore) + " computer " + str(computerScore))
                if (roundsPlayed == int(gameRounds)):
                    if (playerScore > computerScore):
                        print("Congratulations! You won the game!")
                        gameRounds=""
                        break
                    elif (playerScore < computerScore):
                        print("Better luck next time... Computer won the game")
                        gameRounds=""
                        break
                    else:
                        print("Game ended on a tie")
                        gameRounds=""
                        break
            elif (playerChoice == "Rock" and computerChoice == "Rock" or
                  playerChoice == "Scissors" and computerChoice == "Scissors" or
                  playerChoice == "Paper" and computerChoice == "Paper"):
                roundsPlayed += 1
                print("Draw! Nobody scored a point")
                print("The current score is player " + str(playerScore) + " computer " + str(computerScore))
                if (roundsPlayed == int(gameRounds)):
                    if (playerScore > computerScore):
                        print("Congratulations! You won the game!")
                        gameRounds=""
                        break
                    elif (playerScore < computerScore):
                        print("Better luck next time... Computer won the game")
                        gameRounds=""
                        break
                    else:
                        print("Game ended on a tie")
                        gameRounds=""
                        break
            else:
                print("Error: Please try again")


            playerChoice = input("Rock, Paper or Scissors?")
            randomNumber = random.randrange(2)
            computerChoice = computerOptions[randomNumber]
    elif(int(gameRounds) % 2 == 0):
        print("Error: please enter an odd number or press enter to exit")
        gameRounds = input("How many rounds would you like to play? (enter odd number)")


print("Goodbye!")