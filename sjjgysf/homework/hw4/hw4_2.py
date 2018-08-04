# 冒泡排序
def popSort(nums,ascending = True):
	length = len(nums)
	for i in range(length-1,0,-1):
		for j in range(i):
			if nums[j] > nums[j+1]:
				temp = nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = temp
	if not ascending:
		for i in range(length//2-1):
			temp = nums[i]
			nums[i] =  nums[length-1-i]
			nums[length-1-i] = temp
import numpy as np
import random
#nums = np.random.permutation(10)
#nums[3:6] = 100
import unittest
class TestPopSort(unittest.TestCase):
	def setUp(self):
		self._f = popSort
	def testEmpty(self):
		nums = []
		self._f(nums)
		self.assertEqual([],nums)
	def testOne(self):
		nums = [1]
		self._f(nums)
		self.assertEqual(nums,[1])
	def testTwo(self):
		nums = [1,10]
		self._f(nums)
		self.assertEqual(nums,[1,10])
	def testMore(self):
		nums = [1,5,7,9,44,6,8,99,2]
		self._f(nums)
		self.assertEqual(nums,[1,2,5,6,7,8,9,44,99])
	def testDuplicate(self):
		nums = [1,5,0,9,66,7,4,9,3,9]
		self._f(nums)
		self.assertEqual(nums,[0,1,3,4,5,7,9,9,9,66])
unittest.main(argv = ['first-arg-is-ignored'],exit = False)