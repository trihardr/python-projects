import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    max_wins = 3  # First to 3 wins

    while player_score < max_wins and computer_score < max_wins:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        
        if player_choice not in choices:
            print("Invalid input, please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"The computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie! Very nice, no winner yet.")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("Great Success! You win this round.")
            player_score += 1
        else:
            print("The computer wins this round.")
            computer_score += 1

        print(f"Score: You {player_score}, Computer {computer_score}")

        # Check if someone reached 3 wins, but the score is 2-2
        if (player_score == 3 or computer_score == 3) and abs(player_score - computer_score) == 1:
            extend_game = input("Very close! Do you want to continue to first to 5? (yes/no): ").lower()
            if extend_game == "yes":
                max_wins = 5

    if player_score > computer_score:
        print(f"King in the Castle! You won the game with a final score of {player_score} to {computer_score}.")
    else:
        print(f"Great Shame! The computer won the game with a final score of {computer_score} to {player_score}.")

# Start the game
play_game()
