import random

replay = 'y'

# Initialize to variables to store scores
com_score = 0
user_score = 0

while (replay == 'y'):
    user = input("Enter a choice (Rock, Paper, Scissors): ")  
    actions = ["Rock", "Paper", "Scissors"]
    computer = random.choice(actions)
    print(f"\nYou have chosen {user} and Computer has chosen {computer}.\n") # Print the choises

    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "Rock":
        if computer == "Scissors":
            print("Rock smashes Scissors! You win!")
            user_score += 1
        else:
            print("Paper covers Rock! Computer wins.")
            com_score += 1
    elif user == "Paper":
        if computer == "Rock":
            print("Paper covers Rock! You win!")
            user_score += 1
        else:
            print("Scissors cuts Paper! Computer wins.")
            com_score += 1
    elif user == "Scissors":
        if computer == "Paper":
            print("Scissors cuts Paper! You win!")
            user_score += 1
        else:
            print("Rock smashes Scissors! Computer wins.")
            com_score += 1
    print(f'Your score = {user_score}  &  Computer scores = {com_score}') # Print the scores
    replay = input("\nWant to play again? Press y. Else press any other key: \n") # Want to play again?