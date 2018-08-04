import sys 
mins = 101
sums = 0
maxs = -1
print("input n")
n = int(sys.stdin.readline().strip('\n'))
for i in range(n):
	s = float(sys.stdin.readline().strip('\n'))
	if s > maxs:
		maxs = s
	if s < mins:
		mins = s
	sums += s
print(mins,maxs,(sums-maxs-mins)/(n-2))