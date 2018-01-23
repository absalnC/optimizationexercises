from ortools.linear_solver import pywraplp
from ortools.constraint_solver import pywrapcp
solver=pywraplp.Solver("evesteve",pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
#solver=pywrapcp.Solver("evesteve")
timeeve=[4.5,7.8,3.6,2.9]
timesteve=[4.9,7.2,4.3,3.1]
timeeve=[int(t*10) for t in timeeve]
timesteve=[int(t*10) for t in timesteve]
eve=[solver.IntVar(0,1,"eve"+str(x)) for x in range(4)]
steve=[solver.IntVar(0,1,"steve"+str(x)) for x in range(4)]
[solver.Add(eve[i]+steve[i]==1) for i in range(4)]
solver.Add(sum(eve)==2)
solver.Add(sum(steve)==2)
objective=solver.Objective()
[objective.SetCoefficient(eve[i],timeeve[i]) for i in range(4)]
[objective.SetCoefficient(steve[i],timesteve[i]) for i in range(4)]
objective.SetMinimization()
result_status=solver.Solve()
chores=["marketing","cooking","dishwashing","laundry"]
assert result_status==pywraplp.Solver.OPTIMAL
vlist=eve+steve
count=0
for variable in eve:
	if variable.solution_value()==1:
		print("eve does chore: ",chores[count])
	else:
		print("steve does chore:",chores[count])
	count+=1
#	print('%s = %d' % (variable.name(), variable.solution_value()))
#solver.Mini(sum([eve[i]*timeeve[i] for i in range(4)])<=4)
#solver.Minimize(
#	solver.ScalProd(eve,timeeve)+solver.ScalProd(steve,timesteve),1)

