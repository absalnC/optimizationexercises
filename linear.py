from ortools.linear_solver import pywraplp
solver=pywraplp.Solver("linear",pywrapl.Solver.GLOP_LINEAR_PROGRAMMING)
y=solver.NumVar()
