"""
Substring search
input: string s, pattern p
output: index i,j st. s[i:j]=p
"""

class Solution():
	def findPattern(self,s,pattern):
		n=len(s)
		m=len(pattern)
		for i in range(n):
			j=0
			while(i+j<n and j<m):
				if(s[i+j]!=pattern[j]):
					break
				j+=1
			if(j==m):
				return i
		return 0


