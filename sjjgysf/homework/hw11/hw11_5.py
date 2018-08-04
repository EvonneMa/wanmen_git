# 合并k个有序链表
# 可以采用分治算法O(nlgk)
# 也可以使用堆——当指针不够用的时候,换一个思路(每一次比较是O(lgk))
# 这么想的话,用栈似乎也可以,无非在入栈的时候多一次比较,但是时间复杂度就增加了(每一次比较是O(n)),而且还要额外再开辟一个栈
def mergeKSortedLL(lists):
	'''
	本例采用伪代码
	'''
	head = node()
	cnt = head
	q = PriorityQueue()
	for node in lists:
		q.push([node.value,node])
	while not q.isempty():
		# 类似两个链表,这里模拟了n个指针
		cnt.next = q.pop()[1]
		cnt = cnt.next
		if cnt.next:
			q.push([cnt.next.value,cnt.next])
	return head.next