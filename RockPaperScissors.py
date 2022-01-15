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
            if(playerChoice.lower() == "rock" and computerChoice.lower() == "scissors" or
                    playerChoice.lower() == "scissors" and computerChoice.lower() == "paper" or
                    playerChoice.lower() == "paper" and computerChoice.lower() == "rock" ):
                playerScore += 1
                roundsPlayed +=1
                print("you scored a point")
                print("The current score is player " + str(playerScore) + " computer " + str(computerScore))
            elif (playerChoice.lower() == "rock" and computerChoice.lower() == "paper" or
                    playerChoice.lower() == "paper" and computerChoice.lower() == "scissors" or
                    playerChoice.lower() == "scissors" and computerChoice.lower() == "rock"):
                computerScore +=1
                roundsPlayed += 1
                print("The computer scored a point")
                print("The current score is player " + str(playerScore) + " computer " + str(computerScore))
            elif (playerChoice.lower() == "rock" and computerChoice.lower() == "rock" or
                  playerChoice.lower() == "scissors" and computerChoice.lower() == "scissors" or
                  playerChoice.lower() == "paper" and computerChoice.lower() == "paper"):
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
                if (tieBreaker.lower() == "yes"):
                    gameRounds = "1"
                    roundsPlayed = 0
                elif (tieBreaker.lower() == "no"):
                    break
                else:
                    print("Error: enter yes or no")
    else:
        print("Error: please enter a number or press enter to exit")
        gameRounds = input("How many rounds would you like to play?")
print("Goodbye!")