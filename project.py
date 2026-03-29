import random

def user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in choices:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return "You win! Rock beats scissors."
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "You win! Paper beats rock."
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "You win! Scissors beats paper."
    else:
        return "Computer wins!"
    
rounds = int(input("How many rounds do you want to play? "))
user_score = 0
computer_score = 0

while rounds > 0:
    user_choice = user_choice()
    computer_choice = computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1
    
    rounds -= 1

print(f"Final Score - You: {user_score}, Computer: {computer_score}")