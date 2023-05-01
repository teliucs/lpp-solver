from pulp import *
import numpy as np
import matplotlib.pyplot as plt
plt.use('TkAgg')

# Get the number of variables and constraints
num_vars = int(input("How many variables does the problem have? "))
num_cons = int(input("How many constraints does the problem have? "))

# Define the problem
prob = LpProblem("MODEL", LpMaximize)

# Define the decision variables
vars_dict = {}
for i in range(1, num_vars+1):
    vars_dict[f"x{i}"] = LpVariable(name=f"x{i}", lowBound=0)

# Define the objective function
obj_func = LpAffineExpression([(vars_dict[f"x{i+1}"], int(input(f"Enter the coefficient for x{i+1} in the objective function: "))) for i in range(num_vars)])
prob += obj_func

# Define the constraints
for i in range(1, num_cons+1):
    cons_lhs = LpAffineExpression([(vars_dict[f"x{j+1}"], int(input(f"Enter the coefficient for x{j+1} in constraint {i}: "))) for j in range(num_vars)])
    cons_rhs = int(input(f"Enter the value on the right-hand side of constraint {i}: "))
    cons_op = input(f"Enter the relational operator for constraint {i} (<=, ==, or >=): ")
    if cons_op == "<=":
        prob += cons_lhs <= cons_rhs
    elif cons_op == "==":
        prob += cons_lhs == cons_rhs
    else:
        prob += cons_lhs <= cons_rhs
        print("Invalid relational operator. Constraint set to <=.")

# Suppress solver output
LpSolverDefault.msg = False

# Solve the problem
prob.solve()

# Print the optimal solution
print("\nOptimal Solution:")
for i in range(1, num_vars+1):
    print(f"x{i} = {value(vars_dict[f'x{i}'])}") 
print("Optimal objective:", value(prob.objective)) 

# Plot the constraints and the solution
plt.figure()

# Plot the constraints
for i in range(1, num_cons+1):
    cons_lhs = np.array([int(input(f"Enter the coefficient for x{j+1} in constraint {i}: ")) for j in range(num_vars)])
    cons_rhs = int(input(f"Enter the value on the right-hand side of constraint {i}: "))
    if cons_lhs[0] != 0: # if x1 is in the constraint
        x1_vals = np.linspace(0, cons_rhs/cons_lhs[0], 2)
        x2_vals = (cons_rhs - cons_lhs[0]*x1_vals)/cons_lhs[1]
    elif cons_lhs[1] != 0: # if x2 is in the constraint
        x2_vals = np.linspace(0, cons_rhs/cons_lhs[1], 2)
        x1_vals = (cons_rhs - cons_lhs[1]*x2_vals)/cons_lhs[0]
    else:
        print("Invalid constraint. Constraint not plotted.")
    plt.plot(x1_vals, x2_vals, label=f"Constraint {i}")

# Plot the solution
plt.scatter(value(vars_dict["x1"]), value(vars_dict["x2"]), color="red", label="Optimal Solution")

# Set the plot labels and legend
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()

# Show the plot
plt.show()
