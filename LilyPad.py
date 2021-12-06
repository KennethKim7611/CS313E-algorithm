#  File: LilyPad.py

#  Description: Determines the distinct amount of ways Foo can get to the other side
#               of a pond with n lily pads by hopping either 1 or 2 lily pads at a time

#  Student Name: Kenneth Kim

#  Student UT EID: KK34556

#  Course Name: CS 313E

#  Unique Number: 52240

import sys

# Input: n is an int of how many lily pads there are
# Output: return an integer of how many distinct ways there are to cross the pond (order matters)
def distinct_ways(n):
    if n==1 or n==2:
        return n
    '''    
    else:
        return distinct_ways(n-1)+distinct_ways(n-2)
    '''
    j=1
    k=2
    counter = 0
    for i in range(n-2):
        counter = j+k
        j=k
        k= counter
    return counter

def main(): 
    # read number of lily pads

    n = int(input())
    

    # get the result from your call to distinct_ways()
    result = distinct_ways(n)

    # print the result to standard output
    print(result)

if __name__ == "__main__":
    main()