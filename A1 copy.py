#  File: Spiral.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import sys

def create_spiral ( n ):
      arr = [[0 for i in range(n)] for j in range(n)]
      xpos=int(n/2)
      ypos=int(n/2)
      counter=1
      x_positive=True
      y_positive=True
      number=2
      arr[ypos][xpos]=1
      for i in range(2,n*2+1):
            #i is odd then ypos change
            if i==n*2:
                  for j in range(xpos+1,xpos+counter):
                        arr[ypos][j]=number
                        number+=1
            elif i%2!=0:
                  if y_positive==True:
                        for j in range(ypos+1,ypos+1+counter):
                              arr[j][xpos]=number
                              number+=1
                        y_positive=False
                        ypos+=counter
                  else:
                        for j in range(ypos-1,ypos-counter-1,-1):
                              arr[j][xpos]=number
                              number+=1
                        y_positive=True
                        ypos-=counter
                  counter+=1
            #i is evn then xpos change
            else:
                  if x_positive==True:
                        for j in range(xpos+1,xpos+1+counter):
                              arr[ypos][j]=number
                              number+=1
                        x_positive=False
                        xpos+=counter
                  else:
                        for j in range(xpos-1,xpos-counter-1,-1):
                              arr[ypos][j]=number
                              number+=1
                        x_positive=True
                        xpos-=counter
      return arr

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
      n = int(n)
      row_location = 0
      col_location = 0
      for i in range(len(spiral)):
            for j in range(len(spiral)):
                  if n == spiral[i][j]:
                        row_location = i
                        col_location = j
      sum = 0
      for i in range(row_location-1, row_location+2):
            if (i<0) or (i>= len(spiral)):
                  continue
            else:
                  for j in range(col_location-1, col_location+2):
                        if (j<0) or (j>=len(sprial)):
                              continue
                        else:
                              sum+= sprial[i][j]
      sum -=n
      return sum          

def main():
  # read the input file
      num = 11 #int(sys.stdin.readline().strip())
  # create the spiral
      spiral = create_spiral(num)
  # add the adjacent numbers
      print(sum_adjacent_numbers(spiral,int(sys.stdin.readline().strip())))
if __name__ == "__main__": 
  main()