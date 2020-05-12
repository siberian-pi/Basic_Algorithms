"""
Rabin-Karp algorithm
Input: Stirng, Pattern
Return: index of Pattern; -1
2018.11.30
"""
Q=917120411
R=256#base

class Solution():
	def SearchPattern(self,s,p):
		n=len(s)
		m=len(p)
		if(n==0 or m==0):
			return -1
		#value of string p
		vp=0
		vs=0
		vh=1
		for v in p:
			vp=(ord(v)+vp*R)%Q
		for i in range(m-1):
			vh=(vh*R)%Q
		for i in range(n):
			if(i+m>n):
				return -1
			if(i==0):
				for v in s[:m]:
					vs=(ord(v)+vs*R)%Q
			else:
					#update vs
				vs=((vs-vh*ord(s[i-1]))*R+ord(s[i+m-1]))%Q
			if(vs==vp):
	        	#check
	  			for j in range(m):	        		
	  				if(s[i+j]!=p[j]):
	  					break
	  				if(j==m-1):
	  					return i




