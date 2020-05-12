#import BruteSearch as Solver
#import RabinKarp as Solver
import KMP2 as Solver

solver=Solver.Solution()

#read test data
fp=open('data.txt')
data=fp.readlines()
fp.close()

for line in data:
	#standerd results
	Str,Patt,index=line.split(' ')
	index=int(index)

	index_solver=solver.SearchPattern(Str,Patt)

	if(index_solver!=index):
		print("Error!")
		print("String: ",Str)
		print("Pattern: ",Patt)
		print("Expected: ",index," Output: ",index_solver)




