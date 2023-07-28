import random


def get_computer_choice():
    """ Randomly select computer choice from a list of 3 items """
    computer_options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_options)
    return computer_choice


def get_user_choice():
    """ Obtain user input, with basic error checks to ensure valid entry """
    valid_inputs = ["R", "P", "S"]
    user_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    
    while True:
        user_input = input(f"Select Rock, Paper or Scissors: R, P or S > ")
        user_input = user_input.upper()
        # Possible Error: multiple letter entries
        if len(user_input) > 1:
            print(f"You entered: {user_input}")
            print("Please Enter a Single Character")
        # Possible Error: invalid single letter entries
        elif user_input not in valid_inputs:
            print(f"You entered: {user_input}")
            print("Invalid Choice")
        # Valid entries are R, P or S 
        else:
            user_choice = user_dict[user_input]
            return user_choice


def get_winner(computer_choice, user_choice):
    """ Obtain the result of the game, from the perspective of the User """
    # Identify ties between Computer and User    
    if computer_choice == user_choice:
        print("It is a tie!")
    # Identify non-ties, and print the result 
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            print("You Won!")
        elif user_choice == "Scissors":
            print("You lost")
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            print("You Won!")
        elif user_choice == "Rock":
            print("You lost")
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            print("You Won!")
        elif user_choice == "Paper":
            print("You lost")
    

def play():
    """Play the game:
    
    Get the Computers choice,
    Get the User's choice
    Print both 
    Determine and print the Result
    """
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f"User Choice: {user_choice}")
    print(f"Computer Choice: {computer_choice}")
    get_winner(computer_choice, user_choice)


play()
