from ortools.constraint_solver import pywrapcp
solver=pywrapcp.Solver("magic")
x={}
n=3
y=[solver.IntVar(1,n*n,"x{0}{1}".format(i,j)) for i in range(n) for j in range(n)]
print("y")
print(y)
s=15
solver.Add(solver.AllDifferent(y,True))
[solver.Add(solver.Sum([y[i*3+j] for j in range(n)])==s) for i in range(n)]
[solver.Add(solver.Sum([y[i*3+j] for i in range(n)])==s) for j in range(n)]
solver.Add(solver.Sum([ y[i*3+i]     for i in range(n)]) == s) # diag 1
solver.Add(solver.Sum([ y[i*3+n-i-1] for i in range(n)]) == s) # diag 2       
solution=solver.Assignment()
solution.Add(y)
db=solver.Phase(y,solver.CHOOSE_FIRST_UNBOUND,solver.ASSIGN_CENTER_VALUE)
solver.NewSearch(db)
num_solutions = 0
while solver.NextSolution():
    print ("s:", s)
    for i in range(n):
        for j in range(n):
            print (y[i*n+j].Value(),end="")
        print()
    print()
    num_solutions += 1        
print("solution count:",num_solutions)

