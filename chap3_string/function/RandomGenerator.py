import random
import string

def Ran_Str1():
	ran_int=random.randint(1,24)			
	ran_str=''.join(random.sample(string.ascii_letters+string.digits,ran_int))
	return ran_str

def Ran_Str():
	ran_str=''
	for i in range(10):
		ran_int=random.randint(1,24)
		ran_str+=''.join(random.sample(string.ascii_letters+string.digits,ran_int))
	return ran_str

