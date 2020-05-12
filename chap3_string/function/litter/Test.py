"""
Substring search
input: string s, pattern p
output: index i,j st. s[i,j]=p
Test.py
"""

from BruteSearch import Solution
Object=Solution()

fp=open("test_data.txt")
data=fp.readlines()

Input=[]
Output=[]
for line in data:
	string,pattern,index=line.split(' ')
	Input.append([string,pattern])
	Output.append(int(index))

for k in range(len(Input)):
	input_data=Input[k]
	#print(input_data)
	i=Object.findPattern(input_data[0],input_data[1])
	if(i!=Output[k]):
		print("error")
		print(input_data)
		print("expected: ",Output[k], " Output: ",i)





