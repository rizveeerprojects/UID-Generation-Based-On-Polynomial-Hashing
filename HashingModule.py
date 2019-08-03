
#purpose of this file is to generate hash 
class PolynomialHashing:
	def __init__(self):
		pass
	def HashFunction(self,string, mod):
		string=string.upper() #converting all to UPPER CASE LETTER 
		startingCharacter='A' #BASE starting symbol 
		totalAlphabet = 26+15 # hyphen,space, dot, 0-9, (,) 
		base = 1
		value=0
		line=string.split(' ')
		string=""
		for i in line:
			string=string+" "+i 
		for i in range(0,len(string)):
			if(string[i] == ' '): #space 
				diff=0
			elif(string[i] == '-'): #hyphen
				diff = 1
			elif(string[i] == '.'): #dot 
				diff = 2 
			elif(string[i] == '0'): #number map 
				diff = 3
			elif(string[i] == '1'):
				diff = 4
			elif(string[i] == '2'):
				diff = 5
			elif(string[i] == '3'):
				diff = 6
			elif(string[i] == '4'):
				diff = 7
			elif(string[i] == '5'):
				diff = 8
			elif(string[i] == '6'):
				diff = 9
			elif(string[i] == '7'):
				diff = 10
			elif(string[i] == '8'):
				diff = 11
			elif(string[i] == '9'):
				diff = 12
			elif(string[i] == '('):
				diff = 13
			elif(string[i] == ')'):
				diff = 14
			else:
				diff = ord(string[i])-ord(startingCharacter)+15
			value=((value%mod)+(diff%mod * base%mod)%mod)%mod  
			base = (base%mod * totalAlphabet%mod)%mod  
		return value     
