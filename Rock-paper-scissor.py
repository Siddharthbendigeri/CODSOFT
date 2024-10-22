import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please try again.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    if ((user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")):
        return "user"
    else:
        return "computer"
    
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You Chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        if result == "user":
            print("User win this round!")
            user_score += 1
        elif result == "computer":
            print("The computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")
        print(f"Current Score - You: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    if user_score > computer_score:
        print(f"Final result: You win the game! Final Score - You: {user_score}, Computer: {computer_score}")
    elif computer_score > user_score:
        print(f"Final result: The Computer wins the game! Final Score - You: {user_score}, Computer: {computer_score}")
    else:
        print(f"Final result: It's a tie game! Final Score - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()