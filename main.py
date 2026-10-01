import random

def get_cpu_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


    if player == cpu:
        return "tie"
    elif (player == "rock" and cpu == "scissors") or \
         (player == "paper" and cpu == "rock") or \
         (player == "scissors" and cpu == "paper"):
        return "player"
    else:
        return "cpu"

def play_round():

    player_choice = input("Choose rock, paper, or scissors: ").lower()


    while player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        player_choice = input("Choose rock, paper, or scissors: ").lower()

    cpu_choice = get_cpu_choice()
    print(f"CPU chose: {cpu_choice}")


    winner = determine_winner(player_choice, cpu_choice)
    return winner

def play_tournament():
    player_wins = 0
    cpu_wins = 0
    ties = 0

    print("Welcome to Rock, Paper, Scissors — Best of 5 Tournament!")
    print("First to 3 wins takes the trophy.\n")

    while player_wins < 3 and cpu_wins < 3:
        result = play_round()

        if result == "player":
            player_wins += 1
            print("You win this round!")
        elif result == "cpu":
            cpu_wins += 1
            print("CPU wins this round!")
        else:
            ties += 1
            print("This round is a tie!")

        print(f"Score You: {player_wins} | CPU: {cpu_wins} | Ties: {ties}\n")


    if player_wins == 3:
        print(" You win the tournament! Congratulations!")
    else:
        print(" CPU wins the tournament! Better luck next time!")


play_tournament()
