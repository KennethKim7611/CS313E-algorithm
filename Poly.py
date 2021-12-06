#  File: Poly.py

#  Description: Polynomial addition and multiplication

#  Student Name: Kenneth Kim

#  Student UT EID: KK34556

#  Partner Name: Bruce Kim

#  Partner UT EID: bsk674

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 4/12/2021

#  Date Last Modified: 4/12/2021



import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    new_link = Link(coeff,exp)
    current = self.first
    if (current == None):    # if the link is empty
      self.first = new_link
      return
    while (current.next != None):
      current = current.next
    current.next = new_link
    self.sort_list()
  
  def sort_list(self):
    current = self.first
    if current == None:
      return None
    else:
      while current!=None: # sort in order of exp
            index = current.next
            while index!=None:
                  if int(current.exp)< int(index.exp):
                        temp1 = current.exp
                        temp2 = current.coeff
                        current.exp = index.exp
                        current.coeff = index.coeff
                        index.exp = temp1
                        index.coeff = temp2
                  index = index.next
            current = current.next
      current = self.first     
      while current!=None: # sort in order of coeff
            index = current.next
            while index!=None:
                  if int(current.coeff)> int(index.coeff) and int(current.exp)==int(index.exp):
                        temp1 = current.exp
                        temp2 = current.coeff
                        current.exp = index.exp
                        current.coeff = index.coeff
                        index.exp = temp1
                        index.coeff = temp2
                  index = index.next
            current = current.next
      return self
          
  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    poly = {}
    current = self.first
    while current!=None:
          if poly.get(current.exp)!=None:
            poly[current.exp] += int(current.coeff)
          else:
            poly[current.exp] = int(current.coeff)
          current = current.next
    current = p.first
    while current!=None:
          if poly.get(current.exp)!=None:
            poly[current.exp] += int(current.coeff)
          else:
            poly[current.exp] = int(current.coeff)
          current = current.next
    lst=[]
    templst = LinkedList()
    for key, value in poly.items():
      if value ==0:
        continue
      else:
        templst.insert_in_order(value,key)
    templst.sort_list()
    return templst

  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    new_list = LinkedList()
    dummy = LinkedList()
    current = self.first
    while current!=None:
          currentp = p.first
          while currentp!=None:
                new_list.insert_in_order(int(current.coeff)*int(currentp.coeff),int(current.exp)+int(currentp.exp))
                currentp = currentp.next
          current = current.next
    new_list = new_list.add(dummy)
    return new_list
        
        
  # create a string representation of the polynomial
  def __str__ (self):
    current = self.first
    lst = []
    while current != None:
      lst.append(current.coeff)
      lst.append(current.exp)
      current = current.next
    strng =""
    i =0
    while i!= len(lst):
      if i== len(lst)-2:
        strng+="("
        strng+=str(lst[i])
        strng+=", "
        strng+=str(lst[i+1])
        strng+=")" 
      else:
        strng+="("
        strng+=str(lst[i])
        strng+=", "
        strng+=str(lst[i+1])
        strng+=") + "
      i+=2
    return strng

def main():
  # read data from file poly.in from stdin
  # create polynomial p
  line = sys.stdin.readline()
  p = LinkedList()
  for i in range(int(line)):
    line = sys.stdin.readline().split()
    p.insert_in_order(line[0],line[1])
  # create polynomial q
  line = sys.stdin.readline()
  line = sys.stdin.readline()
  q = LinkedList()
  for i in range(int(line)):
    line = sys.stdin.readline().split()
    q.insert_in_order(line[0],line[1])
  # get sum of p and q and print sum
  print(p.add(q))
  # get product of p and q and print product
  print(p.mult(q))
if __name__ == "__main__":
  main()