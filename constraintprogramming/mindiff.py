from ortools.constraint_solver import pywrapcp
def main(unused_argv):
  # Create the solver.
  solver = pywrapcp.Solver("Least diff")

  #
  # declare variables
  #
  digits = list(range(0, 10))
  a = solver.IntVar(digits, "a")
  b = solver.IntVar(digits, "b")
  c = solver.IntVar(digits, "c")
  d = solver.IntVar(digits, "d")
  e = solver.IntVar(digits, "e")

  f = solver.IntVar(digits, "f")
  g = solver.IntVar(digits, "g")
  h = solver.IntVar(digits, "h")
  i = solver.IntVar(digits, "i")
  j = solver.IntVar(digits, "j")

  letters = [a, b, c, d, e, f, g, h, i, j]

  digit_vector = [10000,1000,100,10,1]
  x = solver.ScalProd(letters[0:5],digit_vector)
  y = solver.ScalProd(letters[5:],digit_vector)
  diff = x - y
  
  #
  # constraints
  #
  solver.Add(diff > 0)
  solver.Add(solver.AllDifferent(letters))

  # objective
  objective = solver.Minimize(diff, 1)

  #
  # solution
  #
  solution = solver.Assignment()
  solution.Add(letters)
  solution.Add(x)
  solution.Add(y)
  solution.Add(diff)

  # last solution since it's a minimization problem
  collector = solver.LastSolutionCollector(solution)
  search_log = solver.SearchLog(100, diff)
  # Note: I'm not sure what CHOOSE_PATH do, but it is fast:
  #       find the solution in just 4 steps
  solver.Solve(solver.Phase(letters,
                            solver.CHOOSE_FIRST_UNBOUND,
                            solver.ASSIGN_MIN_VALUE),
               [objective, collector])

  # get the first (and only) solution

  xval = collector.Value(0, x)
  yval = collector.Value(0, y)
  diffval = collector.Value(0, diff)
  print("x:", xval)
  print("y:", yval)
  print("diff:", diffval)
  print(xval, "-", yval, "=", diffval)
  print([("abcdefghij"[i], collector.Value(0, letters[i])) for i in range(10)])
  print()
  print("failures:", solver.Failures())
  print("branches:", solver.Branches())
  print("WallTime:", solver.WallTime())
  print()

if __name__ == "__main__":
  main("cp sample")

  