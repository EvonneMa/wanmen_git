# �����е�k���Ԫ��
# �����ÿ���������(��heapq��)
# �����öѽ��,�ҶѵĴ�СΪk����
import heapq
def findKthLargest(nums,k):
	return heapq.nlargest(k,nums)[-1]
import numpy as np
nums = np.random.permutation(10)
print(findKthLargest(nums,5))