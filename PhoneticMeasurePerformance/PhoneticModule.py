from pyphonetics import Soundex 
from pyphonetics import Metaphone
from pyphonetics import FuzzySoundex
from pyphonetics import Lein
from pyphonetics import RefinedSoundex

#https://stackabuse.com/phonetic-similarity-of-words-a-vectorized-approach-in-python/
#https://pypi.org/project/pyphonetics/

class PhoneticModule:
	def __init__(self):
		self.soundex=Soundex()
		self.metaphone=Metaphone()
		self.fuzzySoundex=FuzzySoundex()
		self.lein=Lein()
		self.refinedSoundex=RefinedSoundex()

		self.phoneticSimilarityWeight={}
		self.phoneticSimilarityWeight['soundex']=0.2
		self.phoneticSimilarityWeight['metaphone']=0.2
		self.phoneticSimilarityWeight['fuzzySoundex']=0.2
		self.phoneticSimilarityWeight['lein']=0.2
		self.phoneticSimilarityWeight['refinedSoundex']=0.2

	def Calculation(self,word1,word2):
		#print(self.soundex.phonetics(word1))
		#print(self.soundex.phonetics(word2))
		res=0.0
		res=self.SoundexMethod(word1,word2) * self.phoneticSimilarityWeight['soundex'] * 1.0
		res=res + self.MetaphoneMethod(word1,word2) * self.phoneticSimilarityWeight['metaphone'] * 1.0 
		res=res + self.FuzzySoundexMethod(word1,word2) * self.phoneticSimilarityWeight['fuzzySoundex'] * 1.0
		res=res + self.LeinMethod(word1, word2) * self.phoneticSimilarityWeight['lein'] * 1.0
		res=res + self.RefinedSoundexMethod(word1, word2) * self.phoneticSimilarityWeight['refinedSoundex'] * 1.0
		print(res)
		return res

	def PhoneticLayerCreation(self,word):
		string=""
		string = self.soundex.phonetics(word)
		string = string + '_' + self.metaphone.phonetics(word)
		string = string + '_' + self.fuzzySoundex.phonetics(word)
		string = string + '_' + self.lein.phonetics(word)
		string = string + '_' + self.refinedSoundex.phonetics(word)
		return string 
	def SoundexMethod(self,word1,word2):
		return self.soundex.distance(word1, word2, metric='levenshtein')
	def MetaphoneMethod(self,word1,word2):
		return self.metaphone.distance(word1, word2, metric='levenshtein')
	def FuzzySoundexMethod(self,word1,word2):
		return self.fuzzySoundex.distance(word1, word2, metric='levenshtein')
	def LeinMethod(self,word1,word2):
		return self.lein.distance(word1, word2, metric='levenshtein')
	def RefinedSoundexMethod(self,word1,word2):
		return self.refinedSoundex.distance(word1, word2, metric='levenshtein')
