#  File: Cipher.py

#  Description: Encrypts and Decrypts given text

#  Student Name: Kenneth Kim

#  Student UT EID: KK34556

#  Partner Name: Bruce Kim

#  Partner UT EID: bsk674

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 2/5/20201

#  Date Last Modified: 2/5/2021


import sys, math
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
  matrix = create_matrix(strng)
  n = len(matrix[0])
  for i in range(n//2):
      for j in range(i, n-i-1):
          temp = matrix[i][j]
          matrix[i][j] = matrix[n-1-j][i]
          matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
          matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
          matrix[j][n-1-i] = temp
  return matrix

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
  matrix = create_matrix(strng)
  return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]
      
def create_matrix(strng):
  m = math.ceil(math.sqrt(len(strng)))**2
  num_ast = m-len(strng)
  strng = strng+num_ast*'*'
  lst = list(strng)
  n = int(m**0.5)
  matrix = [[0 for x in range(n)] for y in range(n)] 
  counter=0
  for i in range(n):
      for k in range(n):
          matrix[i][k]=lst[counter]
          counter+=1
  return matrix

def matrix_to_string(matrix):
  arr_str=''
  for i in matrix:
    for j in i:
      arr_str += str(j)
  return arr_str

def main():
  # read the two strings P and Q from standard imput
  p = sys.stdin.readline().strip()
  q = sys.stdin.readline().strip()
  # encrypt the string P
  print(matrix_to_string(encrypt(p)).replace("*",""))
  # decrypt the string Q
  print(matrix_to_string(decrypt(q)).replace("*",""))
  # print the encrypted string of P and the 
  # decrypted string of Q to standard out
  #print(enc)
  

if __name__ == "__main__":
  main()