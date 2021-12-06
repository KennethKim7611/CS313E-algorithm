 
#  File: Radix.py
 
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
 
class Queue (object):
  def __init__ (self):
    self.queue = []
 
  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)
 
  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))
 
  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)
 
  # return the size of the queue
  def size (self):
    return (len(self.queue))
  
 
# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  queue = []
  for i in range(37):
    queue.append(Queue())
  passes = 0
  for i in a:
    if passes<len(i):
      passes=len(i)
  for i in a:
    queue[10].enqueue(i)
  for i in range(1,passes+1):
    queue = runpass(queue,i)
  output = []
  for i in range(queue[10].size()):
    output.append(queue[10].dequeue())
  a.sort()
  print(a, "This is expected output")
  print()
  return output
 
def getindex(strng,passes):
  if len(strng)<passes:
    return strng[0]
  else:
    return strng[len(strng)-passes:len(strng)-passes+1]  
 
def isalphabet(str):
  return 64<ord(str)<123  
 
def runpass(queue, passes):
  while not queue[10].is_empty():
    strng = queue[10].dequeue()
    index= getindex(strng,passes)
    if isalphabet(str(index)):
      index = ord(index)-86
    else:
      index = int(index)
    queue[index].enqueue(strng)
  for i in range(len(queue)):
    if not i==10: 
      for j in range(queue[i].size()):
        queue[10].enqueue(queue[i].dequeue())
  return queue
 
def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)
 
  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)
 
  '''
  # print word_list
  print (word_list)
  '''
 
  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)
 
  # print the sorted_list
  print (sorted_list)
 
if __name__ == "__main__":
  main()
 
    
 

