# Ä§·¨×Öµä
class magicDict(object):
	def __init__(self):
		self._dic = {}
	def buildDict(self,s):
		for ele in s:
			self._dic[ele] = 
	def search(self,tar):
		for ele in self._dic.items():
			if isSuitable(tar,ele):
				return True
		return False
	def isSuitable(tar,ele):
		k,v = ele
		if abs(len(k) - len(tar)) > 0:
			return False
		for i in range()