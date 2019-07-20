#import modules 
import csv 


#polynomial hashing function 
#Now working on [A-Z],[0-9],[-,., ]
def PolynomialHashing(string,mod):
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


M = int(input("How Many Numbers to use to mod string(do not give space), M = "))
modNumberList=[]
print("Taking input of mod numbers")
for i in range(0,M):
	v = int(input("MOD NUMBER(do not give space): "))
	modNumberList.append(v)
print(modNumberList)


#training file input name 
trainingFilePath = input('Training CSV File Path: ')
#testing file input name 
testingFilePath = input('Testing CSV File Path: ')

COL_NUM = int(input("How many columns to work with in csv files(do not give space): "))
print(COL_NUM) 

STRING_COL_NUM = int(input("How many columns will be hased(do not give space): "))
print(STRING_COL_NUM)
print("Give Name of the columns to be hashed: ")
STRING_COL_NAME=[] 
for i in range(0,STRING_COL_NUM):
	v = input("COL NAME: ")
	STRING_COL_NAME.append(v)
print(STRING_COL_NAME) 

INT_COL_NUM = COL_NUM - STRING_COL_NUM
print("Give Name of the columns not to be hashed: ")
INT_COL_NAME=[]
for i in range(0,INT_COL_NUM):
	v = input("COL NAME: ")
	INT_COL_NAME.append(v)
print(INT_COL_NAME)



trainingDatabaseModified = []  #aka hashed for string attributes, int attributes directly saved 
trainingDatabase = [] #input training object directly saved 
try:
	csvFile = open(trainingFilePath,"r")
	csvReader = csv.DictReader(csvFile)
	print("WARNING: CSV FILE's first line should be column names. For ex - name, father_name, mother_name etc.")
	print("Training Starting") 
	count = 0
	for row in csvReader:
		count = count + 1 
		if(count==1):
			continue
		else:
			objModified={} #hashed object 
			obj={} #real object 
			for i in STRING_COL_NAME:
				obj[i]=row[i] 
				for j in range(0,len(modNumberList)):
					try:
						v = str(PolynomialHashing(obj[i],modNumberList[j]))
						if(j==0):
							hashValue=v 
						else:
							hashValue=hashValue+','+v 
					except Exception as e:
						print(e)
				objModified[i]=hashValue

			for i in INT_COL_NAME:
				obj[i]=row[i]
				objModified[i]=row[i]

			trainingDatabaseModified.append(objModified)
			trainingDatabase.append(obj) 
except Exception as e:
	print(e)
print("Training Completed")
print("Total training instances = ",len(trainingDatabaseModified))
















