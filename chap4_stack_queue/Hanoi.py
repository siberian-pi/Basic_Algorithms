"""
Hanoi(n,from,to,auxi):
"""

class Solution:
	def Hanoi(self,n):
		print(2**n-1)
		self.Hanoi_print(n,'A','C','B')

	def Hanoi_print(self,n,fro,to,auxi):
		if(n==1):
			print(str(1)+" from "+fro+" to "+to)
			return
		else:
			self.Hanoi_print(n-1,fro,auxi,to)
			print(str(n)+" from "+str(fro)+" to "+str(to))
			self.Hanoi_print(n-1,auxi,to,fro)

if __name__ == '__main__':

	Solver=Solution()
	Solver.Hanoi(3)