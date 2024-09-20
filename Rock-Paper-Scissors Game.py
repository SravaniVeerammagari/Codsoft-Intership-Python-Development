import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Main function to play the game
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        # Prompt the user to enter their choice
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        # Get the computer's choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine and display the result
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update the scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display the current scores
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Ask the user if they want to play another round
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

# Start the game
play_game()
