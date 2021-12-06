
#  File: Work.py

#  Description: calculates minimun number of v given line and productivity factor

#  Student Name: Kenneth Kim

#  Student UT EID: KK34556

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 3/4/2021

#  Date Last Modified: 3/4/2021

import sys, math

import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  sum=0
  counter=0
  while v//(k**counter) >0:
    sum+=v//(k**counter)
    counter+=1
  return sum
    

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  start = 0
  while start<=n:
    if sum_series(start,k)>=n:
      return start
    start+=1
  return -1

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  mid = 0
  low = 0
  high = n
  while high>=low:
        mid=(high+low)//2
  if sum_series(mid,k)<n:
      low = mid+1
  elif sum_series(mid,k)>n:
      high = mid-1
  elif sum_series(mid,k)==n:
      return mid
  return mid
      
        


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
