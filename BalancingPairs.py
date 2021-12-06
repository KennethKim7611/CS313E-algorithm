#  File: BalancingPairs.py

#  Description: 

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 

import sys
def balancingPairs(strng):
	balance = 0
	counter = 0
	for i in range(len(strng)):
		if balance==-1: #for protection
			counter+=1
			balance+=1
		if strng[i]=='(':
			balance+=1
		else:
			balance-=1
	return counter+balance

def main():
	# read the input String
	f = sys.stdin
	unbalanced = f.readline().strip()
	print(balancingPairs(unbalanced))


if __name__ == "__main__":
	main()