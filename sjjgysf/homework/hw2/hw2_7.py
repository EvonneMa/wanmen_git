# Ñ°ÕÒ×î³¤×Ö´®
import time
def find_longest(s):
	time1 = time.time()
	start = None
	length = 0
	s_flag = 1
	for i in range(len(s)):
		if s[i] == 1 and s_flag == 1:
			start = i
			s_flag = 0
		if (s[i] == 0 and s_flag == 0) or (s[i] == 1 and i == len(s)):
			s_flag = 1
			length = max(i - start,length)
	time2 = time.time()-time1
	return length,time2
def find_longest2(s):
	time1 = time.time()
	length = maxs = 0
	for i in s:
		length = length + 1 if i == 1 else 0
		maxs = max(length,maxs)
	time2 = time.time()-time1
	return maxs,time2
nums = [1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1]
print(find_longest(nums))
print(find_longest2(nums))