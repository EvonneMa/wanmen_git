# 寻找丢失的数字
# 数组长度n,数字范围1-n
# 嵌套的两个for循环才是O(n^2),如果是串联的则依然是O(n)!!
import time
def test_fun(nums):
	start = time.time()
	find_missing_num(nums)
	t = time.time()-start
	return t
def find_missing_num(s):
	for i in range(len(s)):
		while(s[s[i]-1] != s[i]):
			temp = s[s[i]-1]
			s[s[i]-1] = s[i]
			s[i] = temp
		
	ans = []
	for i in range(len(s)):
		if s[i] != i+1:
			ans.append(i+1)
	return ans
s = [4,3,2,7,8,2,3,1]
#print(find_missing_num(s))
def random_list(l):
	return [[i + 1 for i in range(l * n)] for n in range(1, 20)]
random_lists = random_list(100)
t = []
#print(random_lists)
for l in random_lists:
	t.append(test_fun(l))
print(t)