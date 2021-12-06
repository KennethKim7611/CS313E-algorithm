#  File: Matrix.py

#  Description: Determines if a square 2d list of 1s and 0s has some "symmetry" where the matrix is 
#               the same after one of the following operations: rotate clockwise 90 degrees, rotate 
#               counterclockwise 90 degrees, flip horizontally, or flip vertically

#  Student Name: Kenneth Kim

#  Student UT EID: KK34556

#  Course Name: CS 313E

#  Unique Number: 

import sys, copy

# Prints your 2d list
# Can be used for debugging purposes
def print_arr(temp):
    mx = max((len(str(ele)) for sub in temp for ele in sub))
    for row in temp:
        print(" ".join(["{:<{mx}}".format(ele,mx=mx) for ele in row]))
    print()


# Input: matrix is a 2d square list of 1s and 0s
# Output: return True if a rotation by 90 degrees in either direction (clockwise/counterclockwise)
# or a horizontal/vertical flip results in the matrix being equal to itself.
# return False otherwise
def matrix_has_symmetry(matrix):
    matrix1 = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]
    matrix2 = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0])-1,-1,-1)]
    matrix3 = [[matrix2[j][i] for j in range(len(matrix2))] for i in range(len(matrix2[0])-1,-1,-1)]
    matrixori = [[matrix3[j][i] for j in range(len(matrix3))] for i in range(len(matrix3[0])-1,-1,-1)]
    
    matrix4 = matrix[::-1]
    matrix5 = matrix
    for i in range(0,len(matrix5),1):
        matrix5[i].reverse()
    if ((matrix== matrix1 and matrix1==matrix2) and matrix2==matrix3) or matrix4==matrix or matrix5==matrixori:
        return True
    else:
        return False

def main(): 
    # read dimension of square matrix
    n = int(input())

    matrix = []
    # read data from standard input
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    # get the result from your call to matrix_has_symmetry()
    result = matrix_has_symmetry(matrix)

    # print the result to standard output
    print(result)

if __name__ == "__main__":
    main()