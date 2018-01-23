from ortools.linear_solver import pywraplp
solver=pywraplp.Solver("investments",pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
profits=[17,10,15,19,7,13,9]
required=[43,28,34,48,17,32,23]
investments=[solver.IntVar(0,1,str(i)) for i in range(len(profits))]
c1=solver.Constraint(0,100)
[c1.SetCoefficient(investments[i],required[i]) 
	for i in range(len(profits))]
objective=solver.Objective()
[objective.SetCoefficient(investments[i],profits[i]) for i in range(len(profits))]
objective.SetMaximization()
result_status=solver.Solve()
assert result_status==pywraplp.Solver.OPTIMAL
for i in range(len(investments)):
	if(investments[i].solution_value()==1):
		print("We will invest on project index:",i)