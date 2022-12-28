import random

def get_choices():
    player_choice = input("Enter a choice Rock, Paper, Scissors :").lower()
    options = [ "rock" ,"paper", "scissors" ]
    computer_choice = random.choice(options)
    choices = {"Player" : player_choice , 
                "Computer" : computer_choice}
    return choices

def check_win(player, computer):
    print (f"You chose {player}, and Computer chose {computer} ")
    if player == computer:
        return "Draw"
    elif player == "rock":
        if computer == "scissors":
            return "You won"
        else:
            return "You lose"
    elif player == "scissors":
        if computer == "paper":
            return "You won"
        else:
            return "You lose"
    elif player == "paper":
        if computer == "rock":
            return "You won"
        else:
            return "You lose"
    
choices = get_choices()
result = check_win(choices["Player"], choices["Computer"])
print(result)