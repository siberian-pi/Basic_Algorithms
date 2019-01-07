import random
import string

def Ran_Str():
	ran_str=''
	for i in range(10):
		ran_int=random.randint(1,30)
		ran_str+=''.join(random.sample(string.ascii_letters+string.digits,ran_int))
	return ran_str

for i in range(1,10):
	print(Ran_Str())
