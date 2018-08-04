# Shell排序,时间复杂度根据实际情况而定,应用的不是很多
# 注意：i和j的循环顺序必须是相反的。
#		因为如果i是正向的,j也是正向的,那么j的循环就不能被视为插入排序
#		而是一个简单的冒泡排序了。冒泡排序仅用一个for循环是无法完成的
#		也就是说,我们需要用j的for循环来模拟插入排序
def shellSort(nums,n,step):
	while(step  > 0):
		for i in range(n-step-1,-1,-1):
			for j in range(i+step,n,step):
				if nums[j-step] > nums[j]:
					temp = nums[j]
					nums[j] = nums[j-step]
					nums[j-step] = temp
		#print(nums,step)
		step = step // 2
import numpy as np
n = 10
nums = np.random.permutation(n)
print(nums)
nums[4:8] = 100
shellSort(nums,n,n//2)
print(nums)
	