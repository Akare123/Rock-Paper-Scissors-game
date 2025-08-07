# game.py

import random
import time

def play_game():
    """Main function to run the Rock, Paper, Scissors game."""

    # Initialize scores
    player_score = 0
    computer_score = 0
    
    print("========================================")
    print(" Welcome to Rock, Paper, Scissors! ")
    print("========================================")

    while True:
        # --- Get Player's Choice ---
        player_choice = input("\nChoose rock, paper, or scissors: ").lower()

        # Validate the player's input
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        # --- Get Computer's Choice ---
        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)

        # --- Determine the Winner ---
        print(f"\nYou chose: {player_choice}")
        time.sleep(0.5) # Add a small delay for dramatic effect
        print(f"The computer chose: {computer_choice}")
        time.sleep(1)

        result = ""
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            result = "🎉 You win this round!"
            player_score += 1
        else:
            result = "😭 The computer wins this round!"
            computer_score += 1

        print(f"\n{result}")

        # --- Display Score ---
        print("----------------------------------------")
        print(f"Score: You {player_score} - {computer_score} Computer")
        print("----------------------------------------")

        # --- Ask to Play Again ---
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break # Exit the game loop
    
    print("\nThanks for playing! Final score was:")
    print(f"You: {player_score} | Computer: {computer_score}")
    print("========================================")


# This makes the script runnable
if __name__ == "__main__":
    play_game()
