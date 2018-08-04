# 频率出现次数最高的前k个单词
# 当需要多个排序条件时(如先考虑次数,相同时考虑字母表顺序),此时应当考虑自定义类型
def findKthFreqWord(dic,k):
	#print(dic)
	return heapq.nlargest(k,dic,key = lambda x:x[1])
import heapq
from collections import Counter
words = ['i','love','you','i','like','study','i','love','food']
c = Counter(words)
dic = list(c.items())
#print(c)
ans = findKthFreqWord(dic,2)
print(ans)