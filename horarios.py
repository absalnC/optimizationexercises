from ortools.constraint_solver import pywrapcp
from functools import reduce
import numpy as np

solver=pywrapcp.Solver("test")
hoursweek=25
materias=["esp","mat","hist","cienc","arte"]
ngrupos=["a","b","c","d","e"]
maestros=["luis","ana","joan","maria","betty"]

def printGrupo(horasgrupo):	

	for g in range(5):
		count=0

		print("GRUPO",ngrupos[g])
		for h in range(len(horasgrupo)):
			if(count%5==0):
				print("")
			if horasgrupo[h][g][0].Value()==1:
				print(materias[0],end="\t")
			if horasgrupo[h][g][1].Value()==1:
				print(materias[1],end="\t")
			if horasgrupo[h][g][2].Value()==1:
				print(materias[2],end="\t")
			if horasgrupo[h][g][3].Value()==1:
				print(materias[3],end="\t")
			if horasgrupo[h][g][4].Value()==1:
				print(materias[4],end="\t")
			count+=1
			print("",end="\t")
		print()
		


#tabla grupo-materia(5 grupos y 5 materias)
#grupos=[[[solver.IntVar(0,1,"materia{0},{1}({2})".format(ngrupos[grupo],materias[materia],hora)) for hora in range(hoursweek)] for materia in range(5)] for grupo in range(5)]

#tabla profesor-grupo(5 profesores y 5 grupos)
profesores=[[[solver.IntVar(0,1,"grupo{1},{2}({0})".format(profesor,ngrupos[grupo],hora)) for hora in range(hoursweek)] for grupo in range(5)]for profesor in range(5)]
#extraer grupos
#grupos=[[[profesores[profesor][grupo] for profesor in range(5)] for grupo in range(5)]
flatprof=[profesores[i][j][k] for i in range(5) for j in range(5) for k in range(hoursweek)]

#cada grupo recibe maximo 5 horas de cada materia
[solver.Add(sum(profesores[prof][grupo])==5) for prof in range(5) for grupo in range(5)]

#[solver.Add(sum(grupos[g][m])==5) for g in range(5) for m in range(5)]
#extraer horas grupos
horasgrupo=[[[profesores[profesor][grupo][hora] for profesor in range(5)] for grupo in range(5)]
 for hora in range(hoursweek)]

#horasgrupo=[[grupos[grupo][materia][hora] 
#	for grupo in range(5) for materia in range(5)] for hora in range(hoursweek)] 
#no se pueden traslapar materias del mismo grupo
[solver.Add(sum(horasgrupo[h][grupo])==1) for h in range(hoursweek) for grupo in range(5)]

#extraer horas maestros
horasprof=[[[profesores[profesor][grupo][hora] 
	for grupo in range(5)] for profesor in range(5)] for hora in range(hoursweek)] 
#no se pueden traslapar  horas maestros
[solver.Add(sum(profesor)==1) for hora in horasprof for profesor in hora]
#concatenar grupos iguales de tabla profesor grupo


db=solver.Phase(flatprof,solver.CHOOSE_FIRST_UNBOUND,solver.ASSIGN_MIN_VALUE)
solver.Solve(db)

count=0
while solver.NextSolution():
	count+=1	
	if count==10:
		print("too many solutions")
		break
	print("solution")
	for m in range(len(profesores)):
		print("maestro:",maestros[m])
		for g in range(len(profesores[m])):
			print("grupo:",ngrupos[g])
			for h in range(len(profesores[m][g])):
				print(profesores[m][g][h].Value(),end="")
			print("")
		print("")
	print("---------")
	printGrupo(horasgrupo)
print("num solutions:",count)
			

