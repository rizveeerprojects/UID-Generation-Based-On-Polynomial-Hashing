#import modules 
import csv 
import threading
import functools 



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

hashDictionary={}
try:
	csvFile = open(trainingFilePath,"r")
	csvReader = csv.DictReader(csvFile)
	print("WARNING: CSV FILE's first line should be column names. For ex - name, father_name, mother_name etc.")
	print("Training Starting") 
	count = 0
	for row in csvReader:
		count = count + 1 
		if(count==-1): #not necessary module 
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
				key = i+','+hashValue
				if(key in hashDictionary):
					hashDictionary[key].append(len(trainingDatabase))
				else:
					hashDictionary[key]=[]
					hashDictionary[key].append(len(trainingDatabase))

			for i in INT_COL_NAME:
				obj[i]=int(row[i])
				objModified[i]=int(row[i])
				key=i+','+str(obj[i])
				if(key in hashDictionary):
					hashDictionary[key].append(len(trainingDatabase))
				else:
					hashDictionary[key]=[]
					hashDictionary[key].append(len(trainingDatabase))

			trainingDatabaseModified.append(objModified)
			trainingDatabase.append(obj) 

except Exception as e:
	print(e)
print("Training Completed")
print("Total training instances = ",len(trainingDatabaseModified))


#testing intialization section 

testingDatabaseModified = []  #aka hashed for string attributes, int attributes directly saved 
testingDatabase = [] #input training object directly saved 

try:
	csvFile = open(testingFilePath,"r")
	csvReader = csv.DictReader(csvFile)
	print("WARNING: CSV FILE's first line should be column names. For ex - name, father_name, mother_name etc.")
	print("Testing Starting") 
	count = 0
	for row in csvReader:
		count = count + 1 
		if(count == -1): #not necessary module 
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
				obj[i]=int(row[i])
				objModified[i]=int(row[i])

			testingDatabaseModified.append(objModified)
			testingDatabase.append(obj) 
except Exception as e:
	print(e)

print("Total testing instances = ",len(testingDatabaseModified))



### Thead Module #######
weightAttributes={}
print("Setting weights for string attributes:")
for j in STRING_COL_NAME:
	v= float(input("Weight For attribute "+j+": "))
	weightAttributes[j]=v 

print("Setting weights for integer attributes:")
for j in INT_COL_NAME:
	v= float(input("Weight For attribute "+j+": "))
	weightAttributes[j]=v 

print("Provide Conflicting Measure Threshold: ")
threshold=float(input("Provide CM Threshold: "))

print("Provide MIN_ATTRIBUTE_CONFLICT: ")
MIN_ATTRIBUTE_CONFLICT = int(input(("Minimum number of conflicted attribute to denote a tuple conflicted: ")))

print("Provide +/- Integer Deviation Range For Each Integer Attribute")
INT_COL_DEVIATION={}
for j in INT_COL_NAME:
	v=int(input("Deviation Range For "+j+" : "))
	INT_COL_DEVIATION[j]=v 



class ThreadObject(threading.Thread):
	def __init__ (self,st,en,name):
		threading.Thread.__init__(self)
		self.st = st
		self.en  = en 
		self.name = name 
		self.suggestionList={}
	def run(self):
		global trainingDatabaseModified,testingDatabaseModified
		global trainingDatabase,testingDatabase 

		global STRING_COL_NAME, INT_COL_NAME
		global hashDictionary 

		global weightAttributes,threshold,MIN_ATTRIBUTE_CONFLICT

		for i in range(self.st,self.en+1):
			testInstance = testingDatabaseModified[i] 

			#flag initialization 
			flagList = {}
			conflictedIdx={}
			for j in STRING_COL_NAME:
				flagList[j]=0
				conflictedIdx[j]=[]
			for j in INT_COL_NAME:
				flagList[j]=0
				conflictedIdx[j]=[]

			#flag setting for string attributes
			cm=0 
			for j in STRING_COL_NAME:
				try:
					key=j+','+testInstance[j]
					if(key in hashDictionary):
						flagList[j]=1
						cm=cm+weightAttributes[j]
						conflictedIdx[j]=hashDictionary[key]
					else:
						flagList[j]=0
				except Exception as e:
					print(e)
			#flag setting for int attributes 
			for j in INT_COL_NAME:
				lowRange = max(0,testInstance[j]-INT_COL_DEVIATION[j])
				highRange = testInstance[j]+INT_COL_DEVIATION[j]
				for k in range(lowRange,highRange+1):
					try:
						key=j+','+str(k)
						if(key in hashDictionary):
							conflictedIdx[j].extend(hashDictionary[key])
							if(flagList[j] == 0):
								flagList[j]=1
								cm=cm+weightAttributes[j]

					except Exception as e:
						print(e)

			resultConflictedUIDList=[]
			print("conflict measure = ",cm)
			if(cm>=threshold):
				#conflict exists 
				#list union 
				finalConflictedList=[]
				for j in STRING_COL_NAME:
					if(len(conflictedIdx[j])>0):
						finalConflictedList = list(set(finalConflictedList) | set(conflictedIdx[j])) 
				for j in INT_COL_NAME:
					if(len(conflictedIdx[j])>0):
						finalConflictedList = list(set(finalConflictedList) | set(conflictedIdx[j])) 

				#calculating the actual conflicted UIDs 
				for j in finalConflictedList:
					idx=j
					countConflictedAttr=0 #how many attributes got conflicted in this tuple
					conflictPenalty=0 #amount of conflict penalty based on weight 
					obj=trainingDatabaseModified[idx]
					for k in STRING_COL_NAME:
						if(obj[k] == testInstance[k]):
							conflictPenalty=conflictPenalty+weightAttributes[k]
							countConflictedAttr=countConflictedAttr+1
					for k in INT_COL_NAME:
						diff=abs(obj[k]-testInstance[k])
						if(diff<=INT_COL_DEVIATION[k]):
							conflictPenalty=conflictPenalty+weightAttributes[k]
							countConflictedAttr=countConflictedAttr+1
					if(countConflictedAttr>=MIN_ATTRIBUTE_CONFLICT and conflictPenalty >= threshold):
						# A final conflicted tuple 
						objSave = trainingDatabase[idx]
						objSave['conflictedAttributeWeight']=conflictPenalty
						resultConflictedUIDList.append(objSave)
			else:
				resultConflictedUIDList=[]
			print(str(i) + " Completed")
			self.suggestionList[i]=resultConflictedUIDList  


NUMBER_OF_THREADS=10 #NUMBER OF THREADS 
threadList=[]
division = int(len(testingDatabaseModified)/NUMBER_OF_THREADS)
start=0
cnt=0
while(start<len(testingDatabaseModified)):
	cnt=cnt+1
	en=min(start+division,len(testingDatabaseModified)-1)
	v = ThreadObject(start,en,cnt)
	threadList.append(v)
	start=start+division+1

print("Threads starting")
for i in range(0,len(threadList)):
	threadList[i].start()

for i in range(0,len(threadList)):
	threadList[i].join()
print("Threads Completed")


print("Printing Section")
finalResultList={}
for i in threadList:
	for j in i.suggestionList:
		print(j)
		finalResultList[j]=i.suggestionList[j]
		#print(finalResultList[j])

def customComparator(var1,var2):
	return  var1['conflictedAttributeWeight']>var2['conflictedAttributeWeight']

cmp = functools.cmp_to_key(customComparator)

print("Output Will be written to ResultFile.txt")
f=open("ResultFile.txt","w")
for j in finalResultList:
	print(j)
	row = testingDatabase[j] 
	line=""
	for k in STRING_COL_NAME:
		if(line==""):
			line=row[k]
		else:
			line=line+','+row[k] 
	for k in INT_COL_NAME:
		if(line == ""):
			line=str(row[k])
		else:
			line=line+','+str(row[k])
	f.write(line+'\n')

	line='SuggestionCount:'+str(min(10,len(finalResultList[j])))
	f.write(line+'\n')
	if(len(finalResultList[j])>0):
		finalResultList[j].sort(key=cmp)
		for k in finalResultList[j]:
			line=""
			for key in STRING_COL_NAME:
				if(line == ""):
					line = k[key]
				else:
					line=line+","+k[key]
			for key in INT_COL_NAME:
				if(line==""):
					line=str(k[key])
				else:
					line=line+','+str(k[key])
			f.write('SuggestionList:'+line+'\n')
	else:
		pass 

f.close()


















