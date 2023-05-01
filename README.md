
# Linear Programming Tool

This tool allows you to solve linear programming problems with up to 10 variables and 10 constraints. The tool uses the pulp package to define and solve the problem, and the numpy and matplotlib packages to plot the constraints and solution.


## Installation

1. Install the required packages by running the following command in your command prompt/terminal:

```bash
  pip install pulp numpy matplotlib

```
2. Copy the code into a new Python file and save it with a name of your choice, e.g., "linear_programming.py".

3. Open a command prompt/terminal window and navigate to the directory where the "linear_programming.py" file is saved.

4. Run the following command in the command prompt/terminal:
```bash
  python linear_programming.py
```
5. Input problem details:
- The program will prompt you to enter the number of variables and constraints.
- Follow the prompts to input the coefficients for the objective function and constraints, as well as the right-hand side values and relational operators.

6. View the solution:
- After solving the linear programming problem, the program will display the optimal solution and the objective value.

## Example
```python
How many constraints does the problem have? 3
Enter the coefficient for x1 in the objective function: 1
Enter the coefficient for x2 in the objective function: 2
Enter the coefficient for x1 in constraint 1: 1
Enter the coefficient for x2 in constraint 1: 1
Enter the value on the right-hand side of constraint 1: 3
Enter the relational operator for constraint 1 (<=, ==, or >=): <=
Enter the coefficient for x1 in constraint 2: 2
Enter the coefficient for x2 in constraint 2: -1
Enter the value on the right-hand side of constraint 2: 5
Enter the coefficient for x1 in constraint 3: 3
Enter the coefficient for x2 in constraint 3: 1
Enter the value on the right-hand side of constraint 3: 8

Optimal Solution:
x1 = 1.0
x2 = 2.0
Optimal objective: 5.0

# Then it will ask again for the coefficient of constraints,
# insert them and enjoy your graph
```