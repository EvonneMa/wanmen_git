# 猜数字
import random
import datetime
import sys
def findNum():
	correct = 0
	s = str(datetime.datetime.now())
	s = int(s[11])*int(s[14])*int(s[17])
	num1 = {}
	num2 = {}
	for i in range(4):
		n = random.randint(1,9)
		temp = s % n
		if temp in num1:
			num1[temp].append(i)
		else:
			num1[temp] = [i]
		num2[i] = temp
	while(correct < 4):
		temp = sys.stdin.readline()
		cow = 0
		bull = 0
		for i in range(4):
			n = int(temp[i])
			if n in num1:
				if num2[i] == n:
					bull += 1
				else:
					cow += 1
		correct = cow + bull
		print(bull,' bull(s) and ',cow,' cow(s)')
	print('you win')
findNum()
					 