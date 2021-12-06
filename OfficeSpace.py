#  File: OfficeSpace.py

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
# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    return abs(rect[0]-rect[2])*abs(rect[1]-rect[3])
# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    lst1 = list(rect1)
    lst2 = list(rect2)
    width = []
    height = []
    if (lst1[2] <= lst2[0]) or (lst2[2] <= lst1[0]):
        width = [0,0]
    elif lst1[0] <= lst2[0] <= lst1[2]:
        if lst2[2] <= lst1[2]:
            width = [lst2[2], lst2[0]]
        elif lst2[2] > lst1[2]:
            width = [lst1[2], lst2[0]]
    elif (lst1[0] <= lst2[2] <= lst1[2]) and lst2[0] < lst1[0]:
        width = [lst2[2], lst1[0]]
    elif (lst2[0] < lst1[0]) and (lst1[2] < lst2[2]):
        width = [lst1[2], lst1[0]]
    width.sort()
    if (lst1[3] <= lst2[1]) or (lst2[3] <= lst1[1]):
        height = [0,0]
    elif lst1[1] <= lst2[1] <= lst1[3]:
        if lst2[3] <= lst1[3]:
            height = [lst2[3], lst2[1]]
        elif lst2[3] > lst1[3]:
            height = [lst1[3], lst2[1]]
    elif (lst1[1] <= lst2[3] <= lst1[3]) and lst2[1] < lst1[1]:
        height = [lst2[3], lst1[1]]
    elif (lst2[1] < lst1[1]) and (lst1[3] < lst2[3]):
        height = [lst1[3], lst1[1]]
    height.sort()
    overlap_lst = [width[0], height[0], width[1], height[1]]
    overlap_tup = tuple(overlap_lst)
    return overlap_tup

    
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    counter=0
    for i in range(len(bldg)):
        for j in range(len(bldg[0])):
            if bldg[i][j]==0:
                counter+=1       
    return counter 
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    counter=0
    for i in range(len(bldg)):
        for j in range(len(bldg[0])):
            if bldg[i][j]>1:
                counter+=1   
    return counter
# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    counter=0
    for i in range(len(bldg)):
        for j in range(len(bldg[0])):
            if bldg[i][j]<2:
                counter+=1   
    return counter
# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    x = office[2]
    y = office[3]
    arr = [ [0]*x for i in range(y)]
    for k in range(len(cubicles)):
        for j in range(cubicles[k][1],cubicles[k][3]+1):
            for i in range(cubicles[k][0],cubicles[k][2]):
                arr[j][i]+=1
    arra = arr[::-1]
    for row in arra:
        for elem in row:
            print(elem, end=' ')
        print()
    return arr[::-1]

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases
  assert area ((0,0,2,2)) == 4 
  return "all test cases passed"

def main():
  # read the data
  inp = sys.stdin.readline().strip().split(" ")
  x_max = int(inp[0])
  y_max = int(inp[1])
  office = (0,0,x_max,y_max)
  name = []
  cubicles = []
  n = int(sys.stdin.readline())
  for i in range(n):
    inp = sys.stdin.readline().strip().split(" ")
    name.append(inp[0])
    coord = (int(inp[1]),int(inp[2]),int(inp[3]),int(inp[4]))
    cubicles.append(coord)
  arr = request_space(office,cubicles)
  print("Total",x_max*y_max)
  print("Unallocated",unallocated_space(arr))
  print("Contested",contested_space(arr))
  for i in range(len(name)):
    overlapping_area = 0
    for j in range(n):
        if overlap(cubicles[i],cubicles[j])!=(0,0,0,0) and i !=j:
            overlapping_area+=area(overlap(cubicles[i],cubicles[j]))
    print(name[i],area(cubicles[i])-overlapping_area)

      
      

  # run your test cases
  #print (test_cases())
  # print the following results after computation
  # compute the total office space
  # compute the total unallocated space
  
  # compute the total contested space

  # compute the uncontested space that each employee gets

if __name__ == "__main__":
  main()