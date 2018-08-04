# 水槽问题
# 容量为C,每天灌入l,第i天喝掉i,问第几天能喝干
# 利用数学推导：(1+i)*i/2 >= C-l 求满足条件的i即可
# 可利用二分
def findDay(C,l):
	start = 0
	end = 1
	while(end *(end + 1) / 2 < C - l):
		start = end
		end *= 2
	while(end - start > 0):
		#print(start,end)
		mid = start + (end - start) // 2
		if mid *(mid + 1) / 2 < C - l:
			start = mid + 1
		elif mid *(mid + 1) / 2 > C - l:
			end = mid
		else:
			return mid + l
	return start + l
print(findDay(15,4))
#print(findDay(5,2))