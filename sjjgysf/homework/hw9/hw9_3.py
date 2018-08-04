# 找到第一个只出现一次的字符
from collections import Counter
def findFirstUniqueChar(s):
	dic = {}
	c = Counter(ch for ch in s if ch.isalpha())
	#print(c['a'])
	i = 0
	for ch in s:
		if ch.isalpha() and c[ch] == 1:
			print(ch,i)
			return
		i += 1
	print('No such char')
def findFirstUniqueChar1(s):
	letters = 'abcdefghijklmnopqrstuvwxyz' #该方法扩展性有点差
	indice = [s.index(l) for l in letters if s.count(l) == 1]
	print(min(indice) if indice != [] else -1)
s = 'Hello world, hahe hehe hehe hehe hehe'
findFirstUniqueChar1(s)