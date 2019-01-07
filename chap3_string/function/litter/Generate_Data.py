from function import RandomGenerator
import BruteSearch

solver=BruteSearch.Solution()

fp=open('test_data.txt','a')
for i in range(100):
	ran_str=RandomGenerator.Ran_Str()
	ran_pattern=RandomGenerator.Ran_Str1()
	index=solver.findPattern(ran_str,ran_pattern)
	fp.write(ran_str+' '+ran_pattern+' '+str(index)+'\n')
fp.close()