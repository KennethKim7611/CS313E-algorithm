
#  File: UniqueChars.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

# Input:  alphabet is a list of characters that you will
#         build your strings from.
#         n is an integer and is the length of the unique-character strings
#         that you will need to construct.
# Output: return a list of strings that are length n, are comprised only of
#         characters from alphabet, and have unique characters.
def unique(n, alphabet):
  str1 = ''.join(alphabet)
  lst = all_perms(str1)
  secondlst = []
  print(lst)
  return lst

        

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


# ***There is no reason to change anything below this line***

def main():
  alphabet = sys.stdin.readline().split()
  n = int(sys.stdin.readline())

  result = unique(n, alphabet)
  print("asd")
  result.sort()
  for r in result:
    print(r)

if __name__ == "__main__":
  main()
