from pulp import *

prob = LpProblem("Minimize Food Wastage", LpMinimize)

# Decision Variables
num_items = 3  # Number of food items
x = {i: LpVariable(f"x_{i}", lowBound=0) for i in range(1, num_items + 1)}

D_predicted = 50
D_j = {1: 40, 2: 35, 3: 45}  # Total Daily demand for food items on each day
C = {1: 2, 2: 3, 3: 2.5}  # Cost of preparing one unit of food item i for all i
W_j = {1: 5, 2: 8, 3: 6}  # Total Wastage (in kilograms) of food items on each day
Q_j = {1: 60, 2: 50, 3: 55}  # Quantity (in kilograms) of food items on each day prepared
D_ji = {1: {1: 10, 2: 15, 3: 12},  # Daily demand for food item i on each day observed
         2: {1: 8, 2: 10, 3: 12},
         3: {1: 12, 2: 13, 3: 10}}
w = {1: 0.1, 2: 0.08, 3: 0.12}  # Wastage coefficient of food item i
B = 100  # Budget per day

# Objective Function
prob += lpSum(w[i] * x[i] for i in range(1, num_items + 1))

# Constraints
for i in range(1, num_items + 1):
    prob += x[i] >= min(D_ji[i].values())  # Demand Constraints

prob += lpSum(x.values()) >= D_predicted + 5  # Total food quantity Lower bound (example standard deviation = 5)

prob += lpSum(x[i] * C[i] for i in range(1, num_items + 1)) <= B  # Budget Constraint

prob.solve()

for v in prob.variables():
    print(f"{v.name} = {abs(v.varValue)}")

print(f"Total Wastage: {value(prob.objective)}")
