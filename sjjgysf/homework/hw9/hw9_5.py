# 最小索引和
# 两个列表中相同元素索引之和最小的元素,如有多个都输出
def findMinIndexSum(s1,s2):
	dic = {}
	ans = []
	indice = float('inf')
	for i,ele in enumerate(s1):
		dic[ele] = i
	for i,ele in enumerate(s2):
		if ele in dic:
			if i + dic[ele] < indice:
				ans = [ele]
				indice = i + dic[ele]
			elif i + dic[ele] == indice:
				ans.append(ele)
	print(ans)
#A = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
#B = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
A = ["Shogun", "Burger King", "Tapioca Express", "KFC"]
B = ["KFC", "Burger King", "Shogun"]
findMinIndexSum(A, B)