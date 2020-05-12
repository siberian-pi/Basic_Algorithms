"""
KMP algorithm
Input: Stirng, Pattern
Return: index of Pattern; -1
2018.12.11
"""

class Solution():
	def SearchPattern(self,s,p):
		m=len(p)
		n=len(s)
		prefix=self.Compute_Prefix(p)
		if(m==0 or n==0):#very important
			return -1
	
		q=0#index of p
		i=0#index of s
		for i in range(n):
		
			while(q>0 and p[q]!=s[i]):
				q=prefix[q]
			#print(q," ",m," ",i," ",n)
            #p[q]==s[i]
			if(p[q]==s[i]):
				q+=1
			else:#q==0 and p[q]!=s[i]q==0 
				pass
			if(q==m):
				return i-m+1				


		return -1

	def Compute_Prefix(self,p):
		prefix=[0]
		m=len(p)
		for i in range(m):
			q=i+1
			k=0
			for j in range(q):
				#compare Pq amd Pk
				if(p[q-j:q]==p[:j]):
					k=j
			prefix.append(k)
		return prefix




