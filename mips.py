from ortools.linear_solver import pywraplp
solver=pywraplp.Solver("Integers",pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

x=solver.IntVar(0.0,solver.infinity(),"X")
y=solver.IntVar(0.0,solver.infinity(),"Y")
c1=solver.Constraint(-solver.infinity(),17.5)
c1.SetCoefficient(x,1)
c1.SetCoefficient(y,7)

c2=solver.Constraint(-solver.infinity(),3.5)
c2.SetCoefficient(x,1)
c2.SetCoefficient(y,0)

objective=solver.Objective()
objective.SetCoefficient(x,1)
objective.SetCoefficient(y,10)
objective.SetMaximization()

result_status = solver.Solve()
assert 	result_status==	pywraplp.Solver.OPTIMAL

variable_list = [x, y]

for variable in variable_list:
	print('%s = %d' % (variable.name(), variable.solution_value()))