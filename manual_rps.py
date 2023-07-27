import random

def get_computer_choice():
    computer_options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_options)
    return computer_choice


def get_user_choice():
    valid_inputs = ["R", "P", "S"]
    user_dict = { "R" : "Rock", "P" : "Paper", "S" : "Scissors"}
    
    while True:
        user_input = input(f"Select Rock, Paper or Scissors: Enter R, P or S")
        if user_input.upper() not in valid_inputs: 
            print("Invalid Choice - Please Enter R, P or S (not case-sensitive)")
        else:    
            user_choice = user_dict[user_input.upper()]
            break
    return user_choice