#  File: Reducible.py

#  Description:Finds the longest reducible word using hashing given wordlist

#  Student Name: Kenneth Kim

#  Student UT EID: KK34556

#  Partner Name: Bruce Kim

#  Partner UT EID: bsk674

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 3/30/2021

#  Date Last Modified: 4/2/201

import sys
 
# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False
  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True
 
# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size # Horner's method
  return hash_idx
 
# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
def step_size (s, const):
  return const - hash_word(s,const)
  #cacluate step_size using has_word function with a new const
 
 
# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  idx = hash_word(s, len(hash_table))
  const = 3
  while hash_table[idx] != "": #Meaning while occupied
    idx += step_size(s, const) #double hashing
    idx = idx % len(hash_table)
  hash_table[idx]=s
 
 
# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word (s, hash_table):
  counter =0
  idx = hash_word(s, len(hash_table))
  const = 3
  while hash_table[idx] != "" and counter<len(hash_table): #Meaning while occupied
    if hash_table[idx] == s:  
      return True
    else:
      counter+=1
      idx += step_size(s, const)  #double hashing search
      idx = idx % len(hash_table)
  return False


 
# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  if find_word(s,hash_memo):
    return True
  elif len(s)==1 and not (s =="o" or s=="i" or s=="a"):
    return False
  elif s =="o" or s=="i" or s=="a":
    return True
  #above is base case
  elif not find_word(s,hash_table):
    return False
  else:
    for i in reducible_helper(s): # check possibility of gievn reduced word
      if is_reducible(i,hash_table,hash_memo): # recursion method to go to the most reduced form
          insert_word(s,hash_memo)
          if not find_word(i,hash_memo):
            insert_word(i,hash_memo)
          return True
    return False

def reducible_helper(s): # Given help -> return [elp,hlp,hep,hel]
  lst =[]
  for i in range(len(s)):
    strA=s[0:i]
    strB=s[i+1:len(s)]
    strC=strA+strB
    lst.append(strC)
  return lst

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
 #simple function getting maxlen word
 maxlen = 0
 for i in range(len(string_list)):
      if maxlen<len(string_list[i]):
            maxlen= len(string_list[i]) 
 maxlst=[]
 for i in range(len(string_list)):
        if len(string_list[i])==maxlen:
              maxlst.append(string_list[i])
 maxlst.sort()
 return maxlst

def main():
  # create an empty word_list
  word_list = []
  # read the input
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)
  # find length of word_list
  length = len(word_list)
  # determine prime number N that is greater than twice the length of the word_list
  num_N = 2*len(word_list)+1
  while not is_prime(num_N):
    num_N += 1
  # create an empty hash_list
  hash_list = []
  # populate the hash_list with N blank strings
  for i in range(num_N):
    hash_list.append("")
  # hash each word in word_list into hash_list
  # for collisions use double hashing
  for i in word_list:
    insert_word(i, hash_list)
  # create an empty hash_memo of size M
  hash_memo =[]
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than
  # 0.2 * size of word_list
  num_M = round(len(word_list)*0.2)+10
  while not is_prime(num_M):
    num_M+=1
  # populate the hash_memo with M blank strings
  for i in range(num_M):
    hash_memo.append("")
  # create an empty list reducible_words
  reducible_words = []
  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  for i in word_list:
    if is_reducible(i,hash_list,hash_memo):
      reducible_words.append(i)

  # find the largest reducible words in reducible_words
  maxlst = get_longest_words(reducible_words)
  # print the reducible words in alphabetical order
  # one word per line
  for i in maxlst:
    print(i)

if __name__ == "__main__":
  main()
 
 

#-----------

def collatz_eval(i,j):
    hash_table =[[0,0]]*round(abs(j-i)*1.3)
    for n in range(min(i,j), max(i,j)+1):
        cycle = 0
        c = n
        while c>1:
            hash_val = hash_find(c,hash_table)
            if hash_val !=0 :
                cycle += hash_val-1
                break
            else:
                if c%2 == 0:
                    c = c//2
                else:
                    c = c*3+1
                cycle += 1
        cycle+=1
        hash_insert(n,cycle,hash_table)
    print(hash_table)
    return hash_max(hash_table)
    

def hash_insert(i,j,hash_table):
    index = int(i%3)
    if hash_table[index][0] == 0:
        hash_table[index] = (i,j)
    else:
        while hash_table[index][0] != 0:
            index += 1
        hash_table[index] = (i,j)

def hash_find(n, hash_table):
    index = int(n%3)
    if hash_table[index][0] != 0:
        if hash_table[index][0]==n:
            return hash_table[index][1]
        else:
            while hash_table[index][0]!=0:
                if hash_table[index][0] == n :
                    return hash_table[index][1]
                index +=1
            return 0
    else:
        return 0

def hash_max(hash_table):
    max = 0
    for index in range(len(hash_table)):
        if max < hash_table[index][1]:
            max = hash_table[index][1]
    return max


print(collatz_eval(1,1000))