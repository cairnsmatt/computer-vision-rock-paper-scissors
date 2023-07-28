# Computer Vision RPS

# 
> This project aims to use a [Teachable Machine model](https://teachablemachine.withgoogle.com/) and Python to create a video-based game of ['Rock, Paper, Scissors'](https://en.wikipedia.org/wiki/Rock_paper_scissors). 

## Milestone 1
A GitHub Repo was created and cloned to the local machine.

## Milestone 2
An image-based model was trained using the [Teachable Machine website](https://teachablemachine.withgoogle.com/).

- Image data was captured for Four classes: *Rock*, *Paper*, *Scissors* and *Nothing* (a blank image). At least 200 images were captured for each class.
- The Teachable Machine model was then trained on the four classes, using the default settings.
- Prior to downloading the output files, the performance of the model was tested.  This involved recapturing images for one of the classes, which was not well-recognised.
- The files were downloaded using the default settings from the `Tensor` tab.

After downloading the files, the `keras_model.h5` and `labels.txt` files were staged, committed and pushed to the remote repository.

## Milestone 3

A virtual environment with the necessary dependencies was set up on the local machine.  

This included:
- `opencv-python`, a Python library for image processing and computer vision tasks 
- `tensorflow`, a deep-learning library for Python 
- `ipykernel`, to allow template Jupyter notebooks to be run within the environment

Template Jupyter notebooks with basic code were run to check the downloaded model worked as expected.  
The output of the model is a (1, 4) Numpy array, which assigns a probability (0 to 1) to each of the Four possible Classes (*Rock*, *Paper*, *Scissors* and *Nothing*, respectively)  

 ## Milestone 4
- A Python script was written to simulate a Rock-Paper-Scissors game between the **Computer** and the **User**. 
- This involves X steps:
    - Randomly selecting the **Computer's** choice, using the `random.choice` method in Python.
    - Asking the **User** to select their choice (*R*, *P* or *S*), with error checks to ensure the entry is valid.
    - Determining the result of the game, from the perspective of the **User**
    - Printing the result to the terminal

- After confirming the game functioned correctly, code was tidied to ensure it conforms to the PEP 8 Style Guide.