# -*- coding: utf-8 -*-

import csv 

#purpose of this class is to convert a word according to avro phonetic system 
class AvroPhoneticConversion:
	def __init__(self):
		self.banglaToEnglishMap={}
		self.englishToBanglaMap={}
		self.maxLength=0
		ct=0
		with open('AvroConversion - Sheet1.csv') as csvFile:
			csvReader = csv.DictReader(csvFile)
			for row in csvReader:
				self.banglaToEnglishMap[row['Bangla Character'].strip()]=row['English Phonetic Conversion'].lower().strip()
				self.englishToBanglaMap[row['English Phonetic Conversion'].lower().strip()]=row['Bangla Character'].strip()
				self.maxLength=max(self.maxLength,len(row['Bangla Character'].strip()))

	def Conditions(self,ch1,ch2,ch3):
		try:
			if(ord(ch3) == 2509):
				return 1 #b-fola,z-fola, r-fola, m-fola
		except Exception as e:
			pass
		try:
			if(ord(ch2) == 2509):
				return 2 #we have nukta in center jukto borno or ref
		except Exception as e:
			pass
		try:
			if(ord(ch1) == 2509):
				return 3 #Nukta in front 
		except Exception as e:
			pass		
		return 4 #no nuktas 

	def FolaDetection(self,ch1,ch2,ch3):
		if(ord(ch2) == 2476):
			return 'w' #b-fola
		if(ord(ch2) == 2479):
			return 'y' #z-fola
		if(ord(ch2) == 2480):
			return 'r' #r-fola
		if(ord(ch2) == 2478):
			return 'm' #m-fola

	def JointAlphabetOrRef(self,ch1,ch2,ch3):
		if(ord(ch1) == 2480 and ord(ch2) == 2509):
			return "rr"+self.banglaToEnglishMap[ch3] #ref 
		#joint alphabet
		return self.banglaToEnglishMap[ch1]+self.banglaToEnglishMap[ch3]

	def Conversion(self,word):
		"""
		bstr = "আিমব্য়া"
		for i in bstr:
			print("Count")
			print(i)
			print (repr(i), ord(i))
		"""

		charList=[] #conversion to a list from a string of word 
		print(word)
		for i in word:
			charList.append(i)
		i=len(charList)-1
		result=""
		print(charList)
		while(i>=0):
			ch3=charList[i]
			ch2=""
			if((i-1)>=0):
				ch2=charList[i-1]
			ch1=""
			if((i-2)>=0):
				ch1=charList[i-2]

			print(ch1,ch2,ch3)
			verdict=self.Conditions(ch1,ch2,ch3)
			if(verdict==1):
				string=self.FolaDetection(ch1,ch2,ch3)
				result=string+result
				i=i-2
			elif(verdict==2):
				string=self.JointAlphabetOrRef(ch1,ch2,ch3)
				result=string+result
				i=i-3
			elif(verdict==3):
				ch3=self.banglaToEnglishMap[ch3]
				result=ch3+result
				i=i-1
			elif(verdict==4): 
				ch3=self.banglaToEnglishMap[ch3]
				result=ch3+result
				if(len(ch2) == 0):
					print("result = ",result)
					break
				else:
					ch2=self.banglaToEnglishMap[ch2]
					result=ch2+result
				i=i-2		
		print(result)
		return result
    