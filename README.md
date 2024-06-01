# ROCK PAPER SCISSORS

    #### Video Demo:  <URL HERE>
    #### Description: For the final project, I have created a simple game of rock, paper and scissors which you play against the computer.I have made this game using the tkinter and random module of python.

To play,You can select one of the three options which are rock, paper and scissors.All of the options are displayed alongside their own emojis/pictures. After selecting,press the confirm button to confirm your choice and see if you win or lose based on the option the computer has chosen.It will display the result in the label and it will display the text"You won 🎉" in green if you won and "computer wins" in red if you lost and "draw" in yellow if you and the computer had chosen the same options and the same is done to the emojis. If you want to play again, you can press the reset button in order to start the game again.
The game is located in project.py and i have also created a file to test some of the functions of project.py which is called test_project.py.In project.py, as i have already said , i built the game using tkinter and random module. I have used tkinter to create the main body of the game which includes the window, the buttons, the label , text, etc. The random module is used to choose a random option (rock, paper or scissors) for the computer.I have toggled the buttons so that reset button is disabled if you have not pressed the confirm button once and if you have pressed the confirm button once then the confirm button is disabled and is not enabled until you restart/reset the game and if press the confirm button without having chosen one of the options then nothing will happen and the label will still ask you to choose one of the options.
In project.py, i have implemented various functions like :-

- Rock_command , paper_command and scissor_command -- These are assigned to their respective buttons to display the option the user has chosen.
- Computer -- This function is used to choose the computer's choice and display the option the computer has chosen.
- result -- This is used to find out the result and display it with colors based on the result
- reset -- It is used to reset all of the text, label choices back to normal and the user's and computer's choices to "???"
- confir -- It s used to combine the computer and result functions
  and from line 1 to 31 the window is created and the label are set to normal and all the text is normal too, from line 122 to 132 all the buttons are created.
  In test_project.py, i have implemented some test cases like :-
- copies of rock_command , paper_command and scissor_command
- test_rock_command , test_paper_command and test_scissor_command to test rock_command , paper_command and scissor_command
  \*setup function is used to set up any necessary resources or dependencies before running each test case.
