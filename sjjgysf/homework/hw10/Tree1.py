# 前序+中序->后序
from BST import BST
def postFromInAndPre(pre,mid,post):
	def getPost(pre,mid):
		pres = [pre]
		mids = [mid]
		res = []
		while(mids != []):
			newmids = []
			newpres = []
			length = len(mids)
			for i in range(length):
				pre = pres[i]
				mid = mids[i]
				if pre == []:
					continue
				if len(pre) == 1:
					res.insert(0,pre[0])
					continue
				indice = mid.index(pre[0])
				res.insert(0,pre[0])
				newmids.append(mid[:indice])
				newpres.append(pre[1:indice+1])
				newmids.append(mid[indice+1:])
				newpres.append(pre[indice+1:])
			mids = newmids
			pres = newpres
		return res
	ans = getPost(pre,mid)
	print('Use pre and mid to find post')
	print('my ans = ',ans)
	print('std ans = ',post)
def inFromPostAndPre(pre,mid,post):
	def getMid(pre,post):
		posts = [post]
		pres = [pre]
		res = []
		while(pres != []):
			newpres = []
			newposts = []
			for i in range(len(pres)):
				post = posts[i]
				pre = pres[i]
				if post == []:
					continue
				if len(post) == 1:
					res.append(post[0])
					continue
				length = len(post)
				indice = post.index(pre[1])
				res.append(pre[0])
				newposts.append(post[:indice+1])
				newpres.append(pre[1:2+indice])
				newposts.append(post[indice+1:length - 1])
				newpres.append(pre[indice+2:])
			pres = newpres
			posts = newposts
		return res
	ans = getMid(pre,post)
	print('Use pre and post to find mid')
	print('my ans = ',ans)
	print('std ans = ',mid)
def preFromInAndPost(pre,mid,post):
	def getPre(post,mid):
		posts = [post]
		mids = [mid]
		res = []
		while(mids != []):
			newmids = []
			newposts = []
			for i in range(len(mids)):
				post = posts[i]
				mid = mids[i]
				if post == []:
					continue
				if len(post) == 1:
					res.append(post[0])
					continue
				length = len(post)
				indice = mid.index(post[length-1])
				res.append(post[length-1])
				newmids.append(mid[:indice])
				newposts.append(post[:indice])
				newmids.append(mid[indice+1:])
				newposts.append(post[indice:length-1])
			mids = newmids
			posts = newposts
		return res
	ans = getPre(post,mid)
	print('Use post and mid to find pre')
	print('my ans = ',ans)
	print('std ans = ',pre)
import numpy as np
nums = np.random.permutation(10)
print(nums)
t = BST()
for ele in nums:
	t.add(ele)
pre = t.preloop()
#print(pre)
mid = t.inloop()
post = t.postloop()
postFromInAndPre(pre,mid,post)
inFromPostAndPre(pre,mid,post)
preFromInAndPost(pre,mid,post)