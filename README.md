**Requirements :**

- *Python 3.x* installed on your system. Check if Python is installed by running: *python --version* in command prompt.
- A terminal or command prompt to execute the Python script.
- Code editor such as *VS Code* (optional, for making edits or running the program interactively).

**How to Run the Program :**

**Running the Program in Terminal, Command Prompt, or VS Code**

1. Download or Clone the Project

*Place the **island\_problem.py** file in a directory on your computer.*

1. Open Terminal or Command Prompt / Launch VS Code

*You can either open your terminal/command prompt or launch VS Code and open the script.*

1. Navigate to the Project Directory (if using Terminal or Command Prompt)

*Use the cd command to navigate to the directory where the script is saved.*

*cd path/to/your/directory*


1. Run the Program

*If using the terminal or command prompt, type*

*python island\_problem.py*

*In VS Code, you can use the Run button or press F5 to execute the script in the integrated terminal. Alternatively, you can open the integrated terminal (View > Terminal) and use the same command:*

*python island\_problem.py*

1. Enter Input Data

*The program will first prompt you to enter the number of rows in the matrix. For example, if you want a 3x3 matrix, you will enter:*

*Enter the number of rows: 3*

*Next, the program will ask for the number of columns in the matrix. For a 3x3 matrix, you will enter:*

*Enter the number of columns: 3*

*After that, you will be prompted to enter the matrix row by row. Each row should contain only 0s and 1s, and the values should be separated by spaces. After entering each row, press Enter to proceed to the next one. For example, you can enter:*

*Enter the matrix row by row (0 or 1 only) separated by spaces. After each row, press Enter to proceed to the next one:*

*0 1 1*

*0 0 1*

*1 1 0*


1. View the Result

*Once you have entered the matrix, the program will process it and calculate the size of the largest possible land mass after changing exactly one water cell (1) to a land cell (0). The program will then display the result:*

*Largest possible land mass size after flipping one '1' to '0': 5*

**----------------------------------------------------------------**

*Joining databases*

1. Run the Program

*If using the terminal or command prompt, type*

*python joining\_databases\_baseline.py*

*python joining\_databases\_improved.py*

*In VS Code, you can use the Run button or press F5 to execute the script in the integrated terminal. Alternatively, you can open the integrated terminal (View > Terminal) and use the same command:*

*python joining\_databases\_baseline.py*

*python joining\_databases\_improved.py*

1. Enter Input Data

*Enter elements for list L in the format L=(k,x) separated by space: (3,4) (5,6)*

*Enter elements for list R in the format R=(k,s) separated by space: (3,u) (5,a)*


1. View the Result

*Joined List J:*

*(3, 4, u)*

*(5, 6, a)*


**NOTE:**

- *Each element in list L should be a tuple in the format (k,x) where k, x are integers*
- *Each element in list R should be a tuple in the format (k,s) where k is an integers and s is a string*
- *The tuples should be separated by spaces.*
- *The program ensures that the keys are integers and that the numerical values and string values are of the expected types. If a key is not an integer or if a value is not of the correct type, the program will terminate with an appropriate error message.*

  **-------------------------------------------------------------------------**

  *Shipping Two Items*

1. Run the Program

*If using the terminal or command prompt, type*

*python shipping\_two\_items\_baseline.py*

*python shipping\_two\_items\_optimized.py*

*In VS Code, you can use the Run button or press F5 to execute the script in the integrated terminal. Alternatively, you can open the integrated terminal (View > Terminal) and use the same command:*

*python shipping\_two\_items\_baseline.py*

*python shipping\_two\_items\_optimized.py*

1. Enter Input Data

*When prompted, enter a list of products. Each product should be in the format (price, name), separated by spaces.*

*Example input:*

*(1000, productA) (1500, productB) (1200, productC) (1300, productD)*

1. View the Result

*The program will return either the first pair of products whose combined price equals $2500 or 'NIL' if no such pair is found.*

*Example output:*

*Result: ((1000, 'productA'), (1500, 'productB'))*


**-----------------------------------------------------------------**

**Unique Starting City**

1. Run the Program

*If using the terminal or command prompt, type*

*python unique\_starting\_city.py*

*In VS Code, you can use the Run button or press F5 to execute the script in the integrated terminal. Alternatively, you can open the integrated terminal (View > Terminal) and use the same command:*

*python unique\_starting\_city.py*

1. Enter Input Data

*Input Format: The program will prompt you to enter the following:*

*A list of distances between neighboring cities (e.g., [5, 25, 15, 10, 15]).* 

*A list of fuel available at each city (e.g., [1, 2, 1, 0, 3]).*

*The efficiency of the car in miles per gallon (e.g., 10).*

*Enter road lengths between cities (space-separated): 5 25 15 10 15    #press Enter*

*Enter fuel available at each gas station (space-separated): 1 2 1 0 3  #press Enter*

*Enter car efficiency (MPG): 10   #press Enter*


1. View the Result

*The program will output the index of the optimal starting city, allowing the car to complete the circular journey.*

*The optimal starting city is at index: 4*

















