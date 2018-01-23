from ortools.constraint_solver import pywrapcp
def main():
	solver=pywrapcp.Solver("nqueens")
	board_size=8
	queens= [solver.IntVar(0,board_size -1,"x%i"%i) for i in range(board_size)]
	solver.Add(solver.AllDifferent(queens))

	solver.Add(solver.AllDifferent([queens[i] + i for i in range(board_size)]))
	solver.Add(solver.AllDifferent([queens[i] - i for i in range(board_size)]))
	db=solver.Phase(queens,solver.CHOOSE_FIRST_UNBOUND,solver.ASSIGN_MIN_VALUE)
	solver.NewSearch(db)
	num_sol=0
	while solver.NextSolution():
		for i in range(board_size):
			for j in range(board_size):
				if queens[j].Value()==i:
					print("Q",end=" ")
				else:
					print("_",end=" ")
			print()
		print()
		num_sol+=1
	solver.EndSearch()
	print("Solutions found:", num_sol)
	print("Time:", solver.WallTime(), "ms")
main()