import csv


"""
### SEGMENT 1: Name collection 
### Taking input of all the names ######
names=[]
with open('/home/student/Desktop/PhoneticAccuracyMeasure3/UID-Generation-Based-On-Polynomial-Hashing/TrainingData.csv') as csvFile:
	csvReader = csv.DictReader(csvFile)
	for row in csvReader:
		v=row['name'].split(' ')
		print(v)
		for n in v:
			if(n.strip().upper() not in names):
				names.append(n.strip().upper())
		v=row['father_name'].split(' ')
		for n in v:
			if(n.strip().upper() not in names):
				names.append(n.strip().upper())
		v=row['mother_name'].split(' ')
		for n in v:
			if(n.strip().upper() not in names):
				names.append(n.strip().upper())

print(len(names))
names = sorted(names)

with open('nameFile.csv','w') as csvFile:
	csvWriter = csv.writer( csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	csvWriter.writerow(['name'])
	for i in names:
		print(i)
		csvWriter.writerow([i])
"""

### SEGMENT 2: AFTER REMOVING UNNECESSARY SYMBOLS 
names=[]
with open('nameFile.csv','r') as csvFile:
	csvReader=csv.DictReader(csvFile)
	for row in csvReader:
		n=row['name'].split(' ')
		for i in n:
			#WONT' TAKE NUMBER
			sp=i.strip()
			mainName=""
			for j in sp:
				if(ord(j)>=ord('A') and ord(j)<=ord('Z')):
					mainName=mainName+j
			if(len(mainName)>0 and (mainName not in names)):
				names.append(mainName)
				print(mainName)

names=sorted(names)
with open('nameFile.csv','w') as csvFile:
	csvWriter = csv.writer( csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	csvWriter.writerow(['name'])
	for i in names:
		print(i)
		csvWriter.writerow([i])
print(len(names))






