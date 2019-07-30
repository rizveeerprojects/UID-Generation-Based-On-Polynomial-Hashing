from pyphonetics import Soundex 
from pyphonetics import Metaphone
from pyphonetics import FuzzySoundex
from pyphonetics import Lein
from pyphonetics import RefinedSoundex

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
		res=self.soundex.distance(word1, word2, metric='levenshtein') * self.phoneticSimilarityWeight['soundex'] * 1.0
		res=res + self.metaphone.distance(word1, word2, metric='levenshtein') * self.phoneticSimilarityWeight['metaphone'] * 1.0 
		res=res + self.fuzzySoundex.distance(word1, word2, metric='levenshtein') * self.phoneticSimilarityWeight['fuzzySoundex'] * 1.0
		res=res + self.lein.distance(word1, word2, metric='levenshtein') * self.phoneticSimilarityWeight['lein'] * 1.0
		res=res + self.refinedSoundex.distance(word1, word2, metric='levenshtein') * self.phoneticSimilarityWeight['refinedSoundex'] * 1.0
		print(res)

