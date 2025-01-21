# Requirements :

●	Python 3.x installed on your system. Check if Python is installed by running: python --version in command prompt.
●	A terminal or command prompt to execute the Python script.
●	Code editor such as VS Code (optional, for making edits or running the program interactively).

# How to Run the Program :

Running the Program in Terminal, Command Prompt, or VS Code

1.	Download or Clone the Project

Place the island_problem.py file in a directory on your computer.

2.	Open Terminal or Command Prompt / Launch VS Code

You can either open your terminal/command prompt or launch VS Code and open the script.

3.	Navigate to the Project Directory (if using Terminal or Command Prompt)

Use the cd command to navigate to the directory where the script is saved.

cd path/to/your/directory


4.	Run the Program

If using the terminal or command prompt, type

python island_problem.py

In VS Code, you can use the Run button or press F5 to execute the script in the integrated terminal. Alternatively, you can open the integrated terminal (View > Terminal) and use the same command:

python island_problem.py

5.	Enter Input Data

The program will first prompt you to enter the number of rows in the matrix. For example, if you want a 3x3 matrix, you will enter:

Enter the number of rows: 3

Next, the program will ask for the number of columns in the matrix. For a 3x3 matrix, you will enter:

Enter the number of columns: 3

After that, you will be prompted to enter the matrix row by row. Each row should contain only 0s and 1s, and the values should be separated by spaces. After entering each row, press Enter to proceed to the next one. For example, you can enter:

Enter the matrix row by row (0 or 1 only) separated by spaces. After each row, press Enter to proceed to the next one:
0 1 1
0 0 1
1 1 0


6.	View the Result

Once you have entered the matrix, the program will process it and calculate the size of the largest possible land mass after changing exactly one water cell (1) to a land cell (0). The program will then display the result:

Largest possible land mass size after flipping one '1' to '0': 5
