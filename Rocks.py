import sys

def get_rock_list(rocks):
	if len(rocks)==1 or len(rocks)==0:
		return rocks
	if listchecksign(rocks):
		return rocks
	if checkend(rocks):
		return rocks
	for i in range(len(rocks)-1):
		if not checksign(rocks[i],rocks[i+1]):
			if rocks[i]>0:
				if collision(rocks[i],rocks[i+1]):
					del rocks[i+1] 
				elif abs(rocks[i])==abs(rocks[i+1]):
					del rocks[i]
					del rocks[i]
				else:
					del rocks[i]
	return get_rock_list(rocks)

def checkend(lst):
	negativeidx = -1
	for i in range(len(lst)):
		if lst[i]<0:
			negativeidx = i
	if listchecksignnegative(lst[:negativeidx+1])==True and listchecksignpositive(lst[negativeidx+1:])==True:
		return True
	else: 
		return False
	

def listchecksign(lst):
	if listchecksignnegative(lst)==False and listchecksignpositive(lst) == True:
		return True
	elif listchecksignnegative(lst)==True and listchecksignpositive(lst) == False:
		return True
	else:
		return False


def listchecksignnegative(lst):
	for i in range(len(lst)):
		if  lst[i]>0:
			return False
	return True

def listchecksignpositive(lst):
	for i in range(len(lst)):
		if  lst[i]<0:
			return False
	return True

def checksign(n,m):
	return (n>0 and m>0) or (n<0 and m<0)

def collision(n,m):
	np = n**2
	mp = m**2
	return np>mp

def main():
	rocks = [int(r) for r in sys.stdin.readline().strip().split(" ")]
	result = get_rock_list(rocks)
	print(result)
	
if __name__ == "__main__":
	main()
