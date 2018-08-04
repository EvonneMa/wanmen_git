# Sqrt()
import math
def Sqrt(n,error):
	start = 0
	end = n
	while(True):
		root = start + (end - start) / 2
		temp = root*root - n
		if abs(temp) < error:
			return root
		if temp > 0:
			end = root
		else:
			start = root
print(Sqrt(0,0.000000001))
#print(math.sqrt(10))
		