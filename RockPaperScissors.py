import random

player_score = 0
computer_score = 0
game_rounds = input("How many rounds would you like to play?\n")
rounds_played = 0
computer_options = ["Rock", "Paper", "Scissors"]


while game_rounds != "":
    if game_rounds.isnumeric():
        while rounds_played < int(game_rounds):
            players_choice = input("Rock, Paper or Scissors?\n")
            print("You chose " + players_choice)
            random_number = random.randrange(3)
            computers_choice = computer_options[random_number]
            print("Computer chose " + computers_choice)
            if(players_choice.lower() == "rock" and computers_choice.lower() == "scissors" or
                    players_choice.lower() == "scissors" and computers_choice.lower() == "paper" or
                    players_choice.lower() == "paper" and computers_choice.lower() == "rock"):
                player_score += 1
                rounds_played += 1
                print("you scored a point")
                print("The current score is player " + str(player_score) + " computer " + str(computer_score))
            elif (players_choice.lower() == "rock" and computers_choice.lower() == "paper" or
                  players_choice.lower() == "paper" and computers_choice.lower() == "scissors" or
                  players_choice.lower() == "scissors" and computers_choice.lower() == "rock"):
                computer_score += 1
                rounds_played += 1
                print("The computer scored a point")
                print("The current score is player " + str(player_score) + " computer " + str(computer_score))
            elif (players_choice.lower() == "rock" and computers_choice.lower() == "rock" or
                  players_choice.lower() == "scissors" and computers_choice.lower() == "scissors" or
                  players_choice.lower() == "paper" and computers_choice.lower() == "paper"):
                rounds_played += 1
                print("Draw! Nobody scored a point")
                print("The current score is player " + str(player_score) + " computer " + str(computer_score))
            else:
                print("Error: Please try again")
        if int(game_rounds) == rounds_played:
            if player_score > computer_score:
                print("Congratulations! You won the game!")
                break
            elif player_score < computer_score:
                print("Better luck next time... Computer won the game")
                break
            else:
                print("Game ended on a tie")
                tie_breaker = input("Would you like to play a tie breaker? (enter yes or no)\n")
                if tie_breaker.lower() == "yes":
                    game_rounds = "1"
                    rounds_played = 0
                elif tie_breaker.lower() == "no":
                    break
                else:
                    print("Error: enter yes or no")
    else:
        print("Error: please enter a number or press enter to exit")
        game_rounds = input("How many rounds would you like to play?\n")
print("Goodbye!")