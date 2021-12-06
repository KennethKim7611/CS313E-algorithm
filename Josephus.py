#  File: Josephus.py
 
#  Description: Circular list functions
 
#  Student Name: Bruce Kim
 
#  Student UT EID: bsk674
 
#  Partner Name: Kenneth Kim
 
#  Partner UT EID: KK34556
 
#  Course Name: CS 313E
 
#  Unique Number: 52240
 
#  Date Created: 04/11/21
 
#  Date Last Modified: 04/11/21
import sys
 
class Link (object):
 def __init__(self, data, next = None):
   self.data = data
   self.next = next
 
class CircularList(object):
 # Constructor
 def __init__ (self):
   self.first = None
   
 # Insert an element (value) in the list


 def insert ( self, data ):
   new_link = Link(data)
   current = self.first
   if (current == None):    # if the link is empty
     self.first = new_link
     return
   while (current.next != None):
     current = current.next
   current.next = new_link
 
 
 # Find the Link with the given data (value)
 # or return None if the data is not there
 def find ( self, data ):
   current = self.first
   while current != None:
     if current.data == data:
       return current
     current = current.next
   return None
 
 # Delete a Link with a given data (value) and return the Link
 # or return None if the data is not there
 def delete ( self, data ):
   previous = self.first
   current = self.first
   if (current == None):
     return None
   while (current.data != data):
     if (current.next == None):
       return None
     else:
       previous = current
       current = current.next
   if (current == self.first):
       self.first = self.first.next
   else:
       previous.next = current.next
   return current.data
  
 # Delete the nth Link starting from the Link start
 # Return the data of the deleted Link AND return the
 # next Link after the deleted Link in that order
 def delete_after ( self, start, n ):
   current = self.find(start.data)
   if current==None:
    return None
   count = 1
   while count != n:
     if current.next == None:
       current = self.first
       count += 1
     else:
       current = current.next
       count += 1
   self.delete(current.data)
   return( current.data, self)
 
 
 
 # Return a string representation of a Circular List
 # The format of the string will be the same as the __str__
 # format for normal Python lists
 def __str__ ( self ):
   lst = []
   current = self.first
   if current == None:
     return "[]"
   else:
     while current != None:
       lst.append(current.data)
       current = current.next
   strng ="["
   for i in range(len(lst)):
     strng+=str(lst[i])
     if i != len(lst)-1:
       strng+=", "  
   strng += "]"
   return strng  
 
def main():

 # read number of soldiers
 line = sys.stdin.readline()
 line = line.strip()
 num_soldiers = int (line)
  # read the starting number
 line = sys.stdin.readline()
 line = line.strip()
 start_count = int (line)
 
 # read the elimination number
 line = sys.stdin.readline()
 line = line.strip()
 elim_num = int (line)
 
 # your code
 new_link = CircularList()
 lst = []
 for i in range(num_soldiers):
   lst.append(i+1)
 for i in range (num_soldiers):
   new_link.insert(i+1)
 while new_link.first != None:
   start = new_link.find(start_count)
   x, new_link = new_link.delete_after(start, elim_num)
   lst.remove(x)
   if len(lst) == 0:
     print(x)
   else:
     if x >= max(lst):
       start_count = min(lst)
     else:
       for i in lst:
         if i > x:
           start_count = i
           break
     print(x)
 
 
 
if __name__ == "__main__":
 main()
 

