#  File: BST_Cipher.py
 
#  Description: Encode/Decode input using Binary Search Tree method
 
#  Student Name: Bruce Kim 
 
#  Student UT EID: bsk674
 
#  Partner Name: Kenneth Kim
 
#  Partner UT EID: KK34556
 
#  Course Name: CS 313E
 
#  Unique Number:52240
 
#  Date Created: 04/19/21
 
#  Date Last Modified: 04/20/21
 
# python3 BST_Cipher.py < bst_cipher.in
 
import sys
class Node(object):
 def __init__ (self, data):
   self.data = data
   self.lchild = None
   self.rchild = None
 
class Tree (object):
 # the init() function creates the binary search tree with the
 # encryption string. If the encryption string contains any
 # character other than the characters 'a' through 'z' or the
 # space character drop that character.
 def __init__ (self, encrypt_str):
   output =""
   for i in range(len(encrypt_str)): 
     if encrypt_str[i]==" " or (97<=ord(encrypt_str[i])<=122):
           output+=encrypt_str[i]
   # Remove special characters and keep just alphabetical characters
   self.root = Node(output[0])
   for i in range (1, len(output)):
     self.insert(output[i])
   # insert each characters into the tree
 
 # the insert() function adds a node containing a character in
 # the binary search tree. If the character already exists, it
 # does not add that character. There are no duplicate characters
 # in the binary search tree.
 def insert (self, ch):
   current = self.root
   parent = self.root
   new_node = Node(ch)
   if ch == " ":
         while current.lchild !=None:
               current = current.lchild
         if current.data != " ":
           current.lchild = new_node   
   elif 97 <= ord(ch) <= 122:
     while current != None:
       parent = current
       if ord(ch) < ord(current.data):
         current = current.lchild
         # Keep going left until condition is met
       elif ord(ch) == ord(current.data):
         break
       else:
         current = current.rchild
         # Keep going right until condition is met
     if ord(ch) == ord(parent.data):
       pass
     else:
       if ord(ch) < ord(parent.data):
         parent.lchild = new_node
       elif ord(ch) > ord(parent.data):
         parent.rchild = new_node
         
 
 # the search() function will search for a character in the binary
 # search tree and return a string containing a series of lefts
 # (<) and rights (>) needed to reach that character. It will
 # return a blank string if the character does not exist in the tree.
 # It will return * if the character is the root of the tree.
 def search (self, ch):
   strng = ""
   current = self.root
   if current.data == ch:
     strng += "*"
   else:
     while (current != None) and (current.data != ch):
       if (ord(ch) < ord(current.data)):
         if current.lchild == None:
           return ""
         else:
           current = current.lchild
           strng += "<"
       else:
         if current.rchild == None:
           return ""
         else:
           current = current.rchild
           strng += ">"
   return strng
   # self explanatory code..
 
 # the traverse() function will take string composed of a series of
 # lefts (<) and rights (>) and return the corresponding
 # character in the binary search tree. It will return an empty string
 # if the input parameter does not lead to a valid character in the tree.
 def traverse (self, st):
   if st == "*":
     return self.root.data
  
   current = self.root
   for i in range (len(st)):
     if st[i] == "<":
       if current.lchild == None:
         return ""
       else:
         current = current.lchild
     elif st[i] == ">":
       if current.rchild == None:
         return ""
       else:
         current = current.rchild
   return current.data
  # self explanatory code..
 
 # the encrypt() function will take a string as input parameter, convert
 # it to lower case, and return the encrypted string. It will ignore
 # all digits, punctuation marks, and special characters.
 def encrypt (self, st):
   st = st.lower()
   strng = ""
   for i in range (len(st)):
     if (st[i] == " ") or (97 <= ord(st[i]) <= 122):
       strng += self.search(st[i])
       # Uses search function
       strng += "!"
     else:
       continue
   return strng[:-1]
 
 
 
 
 # the decrypt() function will take a string as input parameter, and
 # return the decrypted string.
 def decrypt (self, st):
   strng = ""
   lst = st.split("!")
   # since ! indicates the end of a character
   for i in lst:
     strng += self.traverse(i)
     # Uses traverse function
   return strng
 
def main():
 # read encrypt string
 line = sys.stdin.readline()
 encrypt_str = line.strip()
 # create a Tree object
 the_tree = Tree (encrypt_str)
 # read string to be encrypted
 line = sys.stdin.readline()
 str_to_encode = line.strip()
 
 # print the encryption
 print (the_tree.encrypt(str_to_encode))
 # read the string to be decrypted
 line = sys.stdin.readline()
 str_to_decode = line.strip()
  # print the decryption
 print (the_tree.decrypt(str_to_decode))
if __name__ == "__main__":
 main()
 

