import numpy as np
from ortools.constraint_solver import pywrapcp
solver=pywrapcp.Solver("sudoku")
tiles=np.matrix([[solver.IntVar(1,4,str([x,y])) for x in range(4)] for y in range(4)])
flat=tiles.flatten().tolist()[0]
#todos los elementos del mismo renglon distintos
subs=[tiles[x:x+2,y:y+2].flatten().tolist()[0] for x in range(0,4,2) for y in range(0,4,2)]
[solver.Add(solver.AllDifferent(gr)) for gr in subs]
[solver.Add(solver.AllDifferent(gr)) for gr  in 
	[tiles[x,:].flatten().tolist()[0] for x in range(4)]]
[solver.Add(solver.AllDifferent(gr)) for gr  in 
	[tiles[:,x].flatten().tolist()[0] for x in range(4)]]

#solution=solver.Assignment()
#solution.Add(flat)

db=solver.Phase(flat,solver.CHOOSE_FIRST_UNBOUND,solver.ASSIGN_MIN_VALUE)
solver.NewSearch(db)
f=np.vectorize(lambda x: x.Value())
count=0
while(solver.NextSolution()):
	#if(count==50):
	#	print("exceeded limit,bye")
	#	break;
	print("Solution")
	values=f(tiles)
	print(values)
	count+=1
print("found solutions:",count)




