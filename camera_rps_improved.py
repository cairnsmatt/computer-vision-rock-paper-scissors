# Rock-Paper-Scissors Game using external webcam

import time
import random
import cv2
from keras.models import load_model
import numpy as np


def get_computer_choice():
    """ Randomly select computer choice from a list of 3 items """
    computer_options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_options)
    return computer_choice


def get_prediction():
    """ Image-based prediction of user choice """
    model = load_model('keras_model.h5', 
                       compile=False)   # suppress compile warning
    # for built-in webcam, change the line below to: cap =cv2.VideoCapture(0) 
    cap = cv2.VideoCapture(1)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    start_time = time.time()
    countdown_message = "Ready?"

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data, 
                                   verbose=0)  # suppresses [=======] - Xs YYms/step 
        cv2.imshow('frame', frame)
        cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)
        cv2.waitKey(25)
        
        # Print countdown output
        elapsed_time = time.time() - start_time
        time_to_start = 10 - elapsed_time
        if time_to_start < 5 and countdown_message == "Ready?": 
            print(countdown_message)
            countdown_message = "3"
        if time_to_start < 3 and countdown_message == "3" : 
            print(countdown_message)
            countdown_message = "2"
        if time_to_start < 2 and countdown_message == "2" :
            print(countdown_message)
            countdown_message = "1"
        if time_to_start < 1 and countdown_message == "1" :
            print(countdown_message)
            countdown_message = "Go!" 
        if time_to_start < 0 and countdown_message == "Go!" :
            print(countdown_message) 
            break

    # Release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()    

    # Match the prediction array to its human readable label 
    classes = { 0: "Rock", 1: "Paper", 2: "Scissors", 3: "Nothing"}
    predicted_class = np.argmax(prediction)
    user_choice = classes[predicted_class]
    return user_choice 


def increment_user():
    """ Simple function used within get_winner to increment user_wins """
    global user_wins
    print("You won that round!")
    user_wins += 1   


def increment_computer():
    """ Simple function used within get_winner to increment computer_wins """
    global computer_wins
    print("You lost that round")
    computer_wins += 1   


def get_winner(computer_choice, user_choice):
    """ Compares user_choice and computer_choice to determine the winner """
    global user_wins, computer_wins
    # Identify ties between Computer and User    
    if computer_choice == user_choice:
        print("It is a tie!")
    # Identify non-ties, and print the result 
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            increment_user()
        elif user_choice == "Scissors":
            increment_computer()
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            increment_user()
        elif user_choice == "Rock":
            increment_computer()
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            increment_user()
        elif user_choice == "Paper":
            increment_computer()
    

def play_round():
    """Play a round of the game:
    
    Get the Computers choice (computer_choice)
    Get the User's choice (user_choice)
    Print both choices
    Determine and print the Result
    """
    computer_choice = get_computer_choice()
    user_choice = get_prediction()
    print(f"You chose {user_choice}")
    print(f"The computer chose {computer_choice}")
    get_winner(computer_choice, user_choice)
    

def play_full_game():
    """ 
    Plays the full game, with variable number of rounds
    Asks the User how many rounds they would like to play.
    Responds, including the number of rounds entered. 
    Then plays the full game 
    The first player to the specified number of wins is the winner.
    """
    
    global user_wins, computer_wins

    user_wins_message = [
         "You were lucky that time!",
         "I'll beat you next time!",
         "There's no way you can do that again!"   
    ]
    computer_wins_message = [
        "Dare to try again?",
        "Too easy! Don't give up the day job!"
        "Terrible tactics!"
    ]

    rounds_to_win = int(input("How many rounds to win the game? >"))
    if rounds_to_win == 1:
        print(f"Sudden Death! Let's do this... \n")
    if rounds_to_win > 1 & rounds_to_win < 5:
        print(f"Ok, first to {rounds_to_win} it is... \n")
    if rounds_to_win > 5:
        print(f"{rounds_to_win} rounds? Could be a long night! \n")

    while user_wins < rounds_to_win and computer_wins < rounds_to_win:
        play_round()
        print(f"Your Score: {user_wins}")
        print(f"Computer Score: {computer_wins}")
        print("")
        if user_wins == rounds_to_win:
            print("You won the match!") 
            print(random.choice(user_wins_message), "\n")   
        if computer_wins == rounds_to_win:
            print("You lost the match!")            
            print(random.choice(computer_wins_message), "\n")


# Set the win counters to 0, then play full game
user_wins = 0
computer_wins = 0
play_full_game()