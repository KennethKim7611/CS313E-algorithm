
#  File: Triangle.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
#combination
def brute_helper(grid, idx, location,each,store):
  if idx == len(grid):
    return store.append(each)
  elif idx == 0:
    return brute_helper(grid, idx+1, location, each + grid[0][0], store)
  else:
    return brute_helper(grid, idx+1, location, each + grid[idx][location], store) or \
     brute_helper(grid, idx+1, location + 1, each + grid[idx][location+1], store)
    

def brute_force (grid):
 idx = 0
 each = 0
 location = 0
 store = []
 brute_helper(grid, idx, location ,each, store)
 return max(store)

# returns the greatest path sum using greedy approach
def greedy (grid):
  sum = 0
  idx = 0
  for i in range(len(grid)):
    max = 0
    temp = 0
    if len(grid[i])<3:
      max = grid[i][0].max(grid[i][1])
      sum+=max
    else:
      for j in range(idx,idx+2):
        if max < grid[i][j]:
          max = grid[i][j]
          temp = j
      sum+=max
      idx = temp
  return sum         

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  return divide_conquer_helper(grid, 0, 0,[])

def divide_conquer_helper(grid, idx, location,mlst):
  if idx == len(grid):
    return 0
  if len(mlst) >= 2 ** len(grid):
    return max(mlst)
  elif idx == 0:
    return mlst.append(grid[0][0]+divide_conquer_helper(grid, idx+1, location,mlst))
  else:
    return grid[idx][location]+divide_conquer_helper(grid,idx+1,location,mlst) or grid[idx][location+1]+divide_conquer_helper(grid,idx+1,location+1,mlst)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  max_path = []
  grid.reverse()
  for i in range (len(grid)-1):
    for j in range(len(grid[i])-1):
      if grid[i][j] >= grid[i][j+1]:
        max_path.append(grid[i][j])
      else:
        max_path.append(grid[i][j+1])
    for k in range (len(max_path)):
      grid[i+1][k] += max_path[k]
    max_path.clear()
  return max(grid[-1])

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  
  # check that the grid was read in properly
  
  
  # output greatest path from exhaustive search
  sublst=[]
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print('The greatest path sum through exhaustive search is \n{}'.format(brute_force(grid)))
  print('The time taken for exhaustive search in seconds is \n{}'.format(times))
  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print('The greatest path sum through greedy search is \n{}'.format(greedy(grid)))
  print('The time taken for greedy approach in seconds is \n{}'.format(times))

  
  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print('The greatest path sum through recursive search is \n{}'.format(divide_conquer(grid)))
  print('The time taken for recursive search in seconds is \n{}'.format(times))
  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print('The greatest path sum through dynamic programming is \n{}'.format(dynamic_prog(grid)))
  print('The time taken for dynamic programminhg in seconds is \n{}'.format(times))

if __name__ == "__main__":
  main()
