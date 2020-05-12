"""
KMP
"""
class Solution():
	def SearchPattern(self,s,p):
		pass

	def Next_List(self,p):
		Next=[0 for x in range(len(p)+1)]
		for q in range(1,len(p)+1,1):
			for t in range(q):
				if(p[:t]==p[q-t:q]):
					Next[q]=t
				break
		return Next

