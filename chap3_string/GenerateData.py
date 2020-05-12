"""
Generate data.txt for testing algorithms
format for data.txt:
string PATTERN index
"""
#Generate string and PATTERN
import random
import string

num_data=100
str_size=20 #max string len 32*str_size
def GenerateSP():
	size=random.randint(2,str_size)
	PATTERN_index=random.randint(1,size-1)
	STRING=''
	PATTERN=''
	for i in range(size):
		ran_str=''.join(random.sample(string.ascii_letters+string.digits,20))
		STRING+=ran_str
		if(i==PATTERN_index):
			PATTERN=ran_str#note that i may not be the least index for PATTERN ran_str
	return STRING,PATTERN
#Using BruteSearch to calculate the index
def BruteSearch(STRING,PATTERN):
	m=len(STRING)
	n=len(PATTERN)
	for i in range(m):
		for j in range(n):
			if(i+j>m-1 or STRING[i+j]!=PATTERN[j]):
				break
			else:
				if(j==n-1):
					return i
	return -1

#wirte data into data.txt
fp=open('data.txt','a+')

for i in range(num_data):
	STRING,PATTERN=GenerateSP()
	index=BruteSearch(STRING,PATTERN)
	fp.write(STRING+' '+PATTERN+' '+str(index)+'\n')

fp.close()
