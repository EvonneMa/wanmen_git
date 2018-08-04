class Node():
	def __init__(self,val,left = None,right = None):
		self.val = val
		self.left = left
		self.right = right
class BST():
	def __init__(self,node = None):
		self.root = node
	
	def add(self,val):
		if self.root.val == None:
			self.root.val = val
		else:
			self.__add(val,self.root)
				
	def __add(self,val,node):
		while(node != None):
			if val == node.val:
				return
			if val > node.val:
				if node.right != None:
					node = node.right
				else:
					node.right = Node(val)
					return
			else:
				if node.left != None:
					node = node.left
				else:
					node.left = Node(val)
					return
	
	def inloop(self):
		return self.__inloop(self.root)
		
	def __inloop(self,node):
		s = []
		res = []
		while(True):
			while(node):
				s.append(node)
				node = node.left
			if len(s) == 0:
				print()
				return res
			node = s.pop()
			res.append(node.val)
			print(node.val,end = '')
			node = node.right
		
		
	def preloop(self):
		ans = self.__preloop(self.root)
		#print('hehe',ans)
		return ans
	
	def __preloop(self,node):
		s = []
		res = []
		i = 0
		while(True):
			while(node):
				res.append(node.val)
				print(node.val,end = '')
				s.append(node)
				node = node.left
			if len(s) == 0:
				print()
				return res
			node = s.pop().right
		
		
	def postloop(self):
		ans = self.__postloop(self.root)
		print()
		return ans
		
	def __postloop(self,node):
		res = []
		stack = [(node,False)]
		while(stack != []):
			node,visited = stack.pop()
			if node:
				if visited:
					res.append(node.val)
					print(node.val,end = '')
				else:
					stack.append((node,True))
					stack.append((node.right,False))
					stack.append((node.left,False))	
		return res
					
	def findFloorAndCeil(self,n):
		self.__findFloorAndCeil(n,self.root)
		
	def __findFloorAndCeil(self,n,node):
		floor = float('-inf')
		ceil = float('inf')
		while(node):
			if node.val == n:
				print('floor = ',n,' and ceil = ',n)
				return
			if node.val < n:
				floor = node.val
				node = node.right
			else:
				ceil = node.val
				node = node.left
		print('floor = ',floor,' and ceil = ',ceil)
		return
def main():
	import numpy as np
	#nums = np.random.permutation(10)
	nums = [1,0,5,6,4,3,8,9,2,7]
	bst = BST()
	print(nums)
	for ele in nums:
		bst.add(ele)
	a = bst.inloop()
	b = bst.preloop()
	c = bst.postloop()		
	nums = [1,0,5,4,6,3,8,2,7,9]
	bst = BST()
	print(nums)
	for ele in nums:
		bst.add(ele)
	a = bst.inloop()
	b = bst.preloop()
	c = bst.postloop()	
	#print('hehe',a,b,c)
	#bst.findFloorAndCeil(7)
	# 不同的顺序,相同的树	
if __name__ == '__main__':
	main()

	