class Solution():
	def SearchPattern(self,s,p):#return index
		n=len(s)
		m=len(p)
		if(m==0 or n==0):
			return -1
		for i in range(n):
			for j in range(m):
				if(i+m>n):
					return -1#no match
				if(s[i+j]!=p[j]):
					break#i+1
				if(j==m-1):
					return i


