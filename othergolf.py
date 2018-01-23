from ortools.constraint_solver import pywrapcp
from functools import reduce

[Bill,Paul,Jack,Frank]=[i for i in range(4)]
names=["Bill","Paul","Jack","Frank"]
lasts=["Clubb","Carter","Green","Sands"]
jobs=["cook","maintenance","clerk","caddy"]


solver=pywrapcp.Solver("golf")

scores=[solver.IntVar(70,85,"scores"+str(x)) for x in range(4)]
#n=[solver.IntVar(0,4,"names"+str(x))for x in range(4)]
l=[solver.IntVar(0,3,"lasts"+str(x)) for x in range(4)]
lindex=[solver.IntVar(0,3,"lindex"+str(x)) for x in range(4)]
[lbill,lpaul,ljack,lfrank]=l
j=[solver.IntVar(0,3,"jobs"+str(x)) for x in range(4)]
jindex=[solver.IntVar(0,3,"jindex"+str(x)) for x in range(4)]
[jbill,jpaul,jjack,jfrank]=j
incognitas=[scores,l,j]
#indices, x[indice[x]]=indice

[ solver.Add( solver.Element(l, lindex[x]) == x ) for x in range(4) ]
[solver.Add(solver.Element(j,jindex[x])==x) for x in range(4)]


#diferentes puntos,trabajos y apellidos
[solver.Add(solver.AllDifferent(x)) for x in incognitas]
#bill no es maintenance
solver.Add(jbill!=1)
#nadie anoto 81
[solver.Add(score!=81) for score in scores]

#bill tiene menor puntaje
#map(lambda x:solver.Add(scores[0]<x),scores[1:])
#solver.Add(scores[Bill] < scores[Jack])
#solver.Add(scores[Bill] < scores[Paul])
#solver.Add(scores[Bill] < scores[Frank])

#mr club no es paul
solver.Add(lpaul!=0)

#mr club tiene 10 puntos mas que clerk
solver.Add(solver.Element(scores,lindex[0])==solver.Element(scores,jindex[2])+10)

#fran no es caddy ni apellida sands, el caddy tampoco apellida sands
solver.Add(jfrank != 3)
solver.Add(lfrank != 3)
solver.Add(solver.Element(l,jindex[3])!=3)

#in some order ...
b3_a_1 = solver.IsEqualVar(solver.Element(scores, lindex[3]) + 4,
                             scores[3])
b3_a_2 = solver.IsEqualVar(solver.Element(scores, jindex[3]),
                             solver.Element(scores, lindex[3]) + 7)

b3_b_1 = solver.IsEqualVar(solver.Element(scores, lindex[3]) + 7,
                             scores[3])
b3_b_2 = solver.IsEqualVar(solver.Element(scores, jindex[3]),
                             solver.Element(scores, lindex[3]) + 4)

#solver.Add((b3_a_1 * b3_a_2) + (b3_b_1 * b3_b_2) == 1)



#Mr Carter tiene 78 puntos
solver.Add(solver.Element(scores,lindex[1])==78)
#El puntaje de Frank es menor al de Mr. Carter
solver.Add(l[3]!=1)
solver.Add(scores[3]<solver.Element(scores,lindex[1]))
#ninguno apunto 81 puntos
[solver.Add(scores[x]!=81) for x in range(4)]
db=solver.Phase(l+j+scores+lindex+jindex,solver.CHOOSE_FIRST_UNBOUND,solver.ASSIGN_MIN_VALUE)
solver.NewSearch(db)
count=0
while solver.NextSolution():
	if(count==1000):
		print("too many solutions, bye")
		break
		print("Solution:")
	for i in range(4):
		print("name:",names[i])
		print("last name:",lasts[l[i].Value()])
		print("index of last name:",lindex[l[i].Value()].Value())
		print("job:",jobs[j[i].Value()])
		print("score:",scores[i].Value())
		print("-----------")
	count+=1
print("total solutions:",count)
