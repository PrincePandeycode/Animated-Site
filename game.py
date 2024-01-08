import random

def simple_ai():
    # Get user input
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Define AI choices
    ai_choices = ['rock', 'paper', 'scissors']
    ai_choice = random.choice(ai_choices)

    # Print AI's choice
    print(f"AI chooses {ai_choice}")

    # Determine the winner
    if user_choice == ai_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and ai_choice == 'scissors') or
        (user_choice == 'paper' and ai_choice == 'rock') or
        (user_choice == 'scissors' and ai_choice == 'paper')
    ):
        print("You win!")
    else:
        print("AI wins!")

# Run the simple AI
simple_ai()
twst.