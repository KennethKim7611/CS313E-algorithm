#  File: TestLinkedList.py

#  Description: Multiple functions related to linked list

#  Student Name: Kenneth Kim

#  Student UT EID: KK34556

#  Partner Name: Bruce Kim

#  Partner UT EID: bsk674

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 4/9/2021 

#  Date Last Modified: 4/9/2021

class Link (object):
  def __init__(self, data, next = None):
   self.data = data
   self.next = next
 
class LinkedList (object):
 # create a linked list
 # you may add other attributes
  def __init__ (self):
   self.first = None
 
 # get number of links
  def get_num_links (self):
   count = 1
   current = self.first
   if current  == None:
     return 0
   while current.next != None:
     current = current.next
     count += 1
   return count
  # add an item at the beginning of the list
  def insert_first (self, data):
   new_link = Link(data)
   new_link.next = self.first
   self.first = new_link
 
  # add an item at the end of a list
  def insert_last (self, data):
   new_link = Link(data)
   current = self.first
  
   if (current == None):    # if the link is empty
     self.first = new_link
     return
   while (current.next != None):
     current = current.next
   current.next = new_link
 
 # add an item in an ordered list in ascending order
 # assume that the list is already sorted
  def insert_in_order (self, data):
   new_link = Link(data)
   current = self.first
   if current == None:
     self.first = new_link
     return
   current = current.next
   previous = self.first
   while current.next != None:
     if previous.data <= new_link.data <= current.data:
       previous.next = new_link
       new_link.next = current
       return
     previous = previous.next
     current = current.next
   current.next = new_link
 
  # search in an unordered list, return None if not found
  def find_unordered (self, data):
   # current is just the location (address) of the memory.
   current = self.first
   # if it is empty
   if (current == None):
     return None
   while current.data != data:
     if current.next == None:
       return None
     else:
       current = current.next
   return current
 
 
 
 # Search in an ordered list, return None if not found
 # similar to unordered, but we may not have to go through all locations
  def find_ordered (self, data):
   current = self.first
   if (current == None):
     return None
 
   while current.data != data:
     if current.next == None:
       return None
     else:
       if current.data > data:
         return None
       current = current.next
   return current
 
 
 # Delete and return the first occurrence of a Link containing data
 # from an unordered list or None if not found
  def delete_link (self, data):
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
   return current
 
 
 # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    current = self.first
    output = []
    while current != None:
      output.append(current.data)
      current = current.next
    strng =""
    for i in range(len(output)):
      if i%10==0 and i!=0:
        strng+="\n"
      elif i!=0:
        strng+="  "   
      strng+=str(output[i])+""
    return strng     

 # Copy the contents of a list and return new list
 # do not change the original list
  def copy_list (self):
   new_link = LinkedList()
   current = self.first
   if current == None:
     return new_link
   while current.next != None:
     new_link.insert_last(current.data)
     current = current.next
   new_link.insert_last(current.data)
   return new_link
 
 
 # Reverse the contents of a list and return new list
 # do not change the original list
  def reverse_list (self):
   new_link= self.copy_list()
   current = new_link.first
   prev = None
   while current !=None:
    nxt = current.next
    current.next = prev
    prev=current
    current=nxt
   new_link.first=prev
   return new_link
 
 
 
 # Sort the contents of a list in ascending order and return new list
 # do not change the original list
  def sort_list (self):
   new_list = self.copy_list()
   current = new_list.first
   if current == None:
      return None
   else:
      while current!=None:
            index = current.next
            while index!=None:
                  if current.data> index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                  index = index.next
            current = current.next
      return new_list

 # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
   current = self.first
   if (current == None):
        return True
   while(current.next != None):
        t = current
        if (t.data >= t.next.data):
            return False;
        current = current.next
   return True
 
 # Return True if a list is empty or False otherwise
  def is_empty (self):
   if self.first == None:
     return True
   return False
 
 # Merge two sorted lists and return new list in ascending order
 # do not change the original lists
  def merge_list (self, other):
    new_list = LinkedList()
    ca = self.first
    cb = other.first
    while ca != None:
      new_list.insert_last(ca.data)
      ca = ca.next
    while cb != None:
      new_list.insert_last(cb.data)
      cb = cb.next
    new_list = new_list.sort_list()
    return new_list
 
 # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    a = self.first
    b = other.first
    while (a!=None and b!=None):
      if (a.data != b.data):
        return False
      a = a.next
      b = b.next
    return (a==None and b==None)    
 
 # Return a new list, keeping only the first occurence of an element
 # and removing all duplicates. Do not change the order of the elements.
 # do not change the original list
  def remove_duplicates (self):
    new_link= self.copy_list()
    current = new_link.first
    if current == None:
      return None
    duplicate = []
    while current !=None:
      if current.data in duplicate:
        new_link.delete_link(current.data) 
      else:
        duplicate.append(current.data)
      current = current.next
    new_link = new_link.sort_list()
    return new_link

 
def main():
  l = LinkedList()
  l.insert_last(2)
  l.insert_last(4)
  l.insert_last(6)
  l.insert_last(8)
  k = LinkedList()
  k.insert_last(1)
  k.insert_last(3)
  k.insert_last(5)
  k.insert_last(7)
  print(l.merge_list(k))
 # Test methods insert_first() and __str__() by adding more than
 # 10 items to a list and printing it.
 
 # Test method insert_last()
 
 # Test method insert_in_order()
 
 # Test method get_num_links()
 
 # Test method find_unordered()
 # Consider two cases - data is there, data is not there
 
 # Test method find_ordered()
 # Consider two cases - data is there, data is not there
 
 # Test method delete_link()
 # Consider two cases - data is there, data is not there
 
 # Test method copy_list()
 
 # Test method reverse_list()
 
 # Test method sort_list()
 
 # Test method is_sorted()
 # Consider two cases - list is sorted, list is not sorted
 
 # Test method is_empty()
 
 # Test method merge_list()
 
 # Test method is_equal()
 # Consider two cases - lists are equal, lists are not equal
 
 # Test remove_duplicates()
 
if __name__ == "__main__":
 main()
 
 

