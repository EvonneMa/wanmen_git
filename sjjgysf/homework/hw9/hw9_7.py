# 快乐数
# 自身每一位数字平方和相加等于1则为快乐数,否则不是(重复计算下去)
def findHappyNum(n):
	temp = set()
	s = str(n)
	total = 0
	for ele in s:
		total += int(ele)*int(ele)
	while(total != 1 and total not in temp):
		temp.add(total)
		s = str(total)
		total = 0
		for ele in s:
			total += int(ele)*int(ele)
	if total == 1:
		return True
	return False
n = 19
print(findHappyNum(n))