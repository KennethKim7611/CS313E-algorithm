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
def create_spiral ( n ):
    if n%2==0:
          n+=1
    arr = [[0 for i in range(n)] for j in range(n)] 
    final_value=n*n
    xpos=int(n/2)
    ypos=int(n/2)
    x_plus=True
    y_plus=True
    counter=1
    arr[ypos][xpos]=1
    xpos+=1
    for n in range(2,final_value+1): 
          #Odd
          if n%2==0:
                if x_plus==True:
                      print('Odd addition')
                      for i in range(xpos,xpos+counter):
                            arr[ypos][i]=n
                            n+=1
                      xpos+=counter
                      x_plus=False
                else:
                      print('Odd Subtraction')
                      for i in range(xpos-counter,xpos):
                            arr[ypos][i]=n
                            n+=1
                      xpos-=counter
                      x_plus=True
          #Even
          else:
                if y_plus==True:
                      print('Even Addition')
                      for i in range(ypos,ypos+counter):
                            arr[i][xpos]=n
                            n+=1
                      ypos+=counter
                      y_plus=False
                else:
                      print('Even Subtraction')
                      for i in range(ypos-counter,ypos):
                            arr[i][xpos]=n
                            n+=1
                      ypos-=counter
                      y_plus=True
          for row in arr: 
            print(row) 
          print(n)
          print('')
    #for row in arr: 
     # print(row) 

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
    print("h")

def main():
  # read the input file
    f = open("spiral.in", "r")
  # create the spiral
    sprial = create_spiral(int(f.readline()))
  # add the adjacent numbers

  # print the result

if __name__ == "__main__":
  main()