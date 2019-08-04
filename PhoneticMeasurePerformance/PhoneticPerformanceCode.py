#Main goal of this file is to measure performance of phonetic similarity 
from PhoneticModule import PhoneticModule
import csv


class PhoneticPerformance:
	def __init__(self,wordFileName,minPhoneticEditDistance,phoneticMeasureName, outputFileName):
		self.wordFileName=wordFileName
		self.minPhoneticEditDistance=minPhoneticEditDistance
		self.phoneticMeasureName=phoneticMeasureName
		self.outputFileName=outputFileName


		self.phoneticModule=PhoneticModule()
		self.words=[]
		self.photeticallySimilarWords={}
		
		with open(self.wordFileName) as csvFile:
			csvReader=csv.DictReader(csvFile)
			for row in csvReader:
				self.words.append(row['name'])
				finalList=[]
				for i in range(0,minPhoneticEditDistance): #at least 1, so if minPhoneticEditDistance = 3, then we need to put 0,1,2 
					tempList=[]
					finalList.append(tempList) 
				self.photeticallySimilarWords[row['name']]=finalList

	def Process(self):
		for i in range(0,len(self.words)):
			baseWord=self.words[i]
			for j in range(0,len(self.words)):
				checkingWord=self.words[j]
				if(baseWord == checkingWord):
					continue
				res=0.0
				print(baseWord,checkingWord)
				if(self.phoneticMeasureName=="soundex"):
					try:
						res=self.phoneticModule.SoundexMethod(baseWord,checkingWord) 
					except Exception as e:
						print(e)
						res=self.minPhoneticEditDistance+5
				if(self.phoneticMeasureName=="metaphone"):
					try:
						res=self.phoneticModule.MetaphoneMethod(baseWord,checkingWord)
					except Exception as e:
						print(e)
						res=self.minPhoneticEditDistance+5
				if(self.phoneticMeasureName=="fuzzy soundex"):
					try:
						res=self.phoneticModule.FuzzySoundexMethod(baseWord,checkingWord)
					except Exception as e:
						print(e)
						res=self.minPhoneticEditDistance+5
				if(self.phoneticMeasureName=="lein"):
					try:
						res=self.phoneticModule.LeinMethod(baseWord,checkingWord)
					except Exception as e:
						print(e)
						res=self.minPhoneticEditDistance+5
				if(self.phoneticMeasureName=="refined soundex"):
					try:
						res=self.phoneticModule.RefinedSoundexMethod(baseWord,checkingWord)
					except Exception as e:
						print(e)
						res=self.minPhoneticEditDistance+5
					
				if(res<self.minPhoneticEditDistance):
					print(res)
					print(self.phoneticModule.soundex.phonetics(baseWord))
					print(self.phoneticModule.soundex.phonetics(checkingWord))
					self.photeticallySimilarWords[baseWord][res].append(checkingWord)

	def OutputFileWriting(self):
		with open(self.outputFileName,'w') as csvFile:
			csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			_list=['name']
			for i in range(0,self.minPhoneticEditDistance):
				_list.append(str(i))
			csvWriter.writerow(_list)
			for i in self.photeticallySimilarWords:
				_list=[]
				_list.append(i)
				for j in range(0,self.minPhoneticEditDistance):
					_list.append(self.photeticallySimilarWords[i][j])
					csvWriter.writerow(_list)


#obj = PhoneticPerformance("nameFile.csv",3,"soundex",'SoundexOutput.csv') #so phonetic similar at 0,1 and 2 will be reported
#obj.Process()
#obj.OutputFileWriting()

obj=PhoneticModule()

print(obj.soundex.phonetics('joya'))
print(obj.soundex.phonetics('zoya')) 


print(obj.metaphone.phonetics('joya'))
print(obj.metaphone.phonetics('zoya')) 

print(obj.fuzzySoundex.phonetics('joya'))
print(obj.fuzzySoundex.phonetics('zoya')) 

print(obj.lein.phonetics('joya'))
print(obj.lein.phonetics('zoya')) 

print(obj.refinedSoundex.phonetics('joya'))
print(obj.refinedSoundex.phonetics('zoya')) 