#  File: TestBinaryTree.py
 
#  Description: Functions about Binary Tree
 
#  Student Name: Bruce Kim 
 
#  Student UT EID: bsk674
 
#  Partner Name: Kenneth Kim
 
#  Partner UT EID: KK34556
 
#  Course Name: CS 313E
 
#  Unique Number:52240
 
#  Date Created: 04/26/21
 
#  Date Last Modified: 04/26/21
 


import sys
SPACE = 5
class Queue (object):
    def __init__ (self):
        self.queue = []
    # add an item to the end of the Queue
    def enqueue (self, item):
        self.queue.append(item)
    # remove an item from the beginning of the Queue
    def dequeue(self):
        return self.queue.pop(0)
    # check if the queue is empty
    def is_empty (self):
        return len(self.queue) == 0
    # return the size of the queue
    def size(self):
        return (len(self.queue))

class Node (object):
  def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
  def __init__(self):
    self.root=None
  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)
    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
            current = current.lchild
        else:
            current = current.rchild
      if (val < parent.data):
        parent.lchild = newNode
      else:
        parent.rchild = newNode

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
    # Both empty
    if self.root is None and pNode.root is None:
        return True 
    # One is empty
    if self.root is None and pNode.root is not None:
        return False
    if self.root is not None and pNode.root is None:
        return False
    # Else
    # Uses stack to check if each node is equal to each other
    stack = []
    stack.append((self.root, pNode.root))
    while stack:
        self.root, pNode.root = stack.pop()
        if self.root.data != pNode.root.data:
            return False
        if self.root.lchild and pNode.root.lchild:
            stack.append((self.root.lchild, pNode.root.lchild))
        elif self.root.lchild or pNode.root.lchild:
            return False
        if self.root.rchild and pNode.root.rchild:
            stack.append((self.root.rchild,pNode.root.rchild))
        elif self.root.rchild or pNode.root.rchild:
            return False
    return True

  # Returns a list of nodes at a given level from left to right
  def get_level (self, level): 
    # Uses queue to process each level 
    num = 0
    lst = []
    queue = Queue()
    queue2 = Queue()
    if self.root == None:
      return lst
    queue.enqueue(self.root)
    
    while not queue.is_empty():
      if num == level: # When level is reached add each node to the lst and return
        for i in range (queue.size()):
          node = queue.dequeue()
          lst.append(node)
        return lst

      # Dequeue following level and queue following levels
      while not queue.is_empty(): 
        node = queue.dequeue()
        if node.lchild != None:
          queue2.enqueue(node.lchild)
        if node.rchild != None:
          queue2.enqueue(node.rchild)
      queue = queue2
      temp = Queue()
      queue2 = temp
      num += 1
    return []



  # Returns the height of the tree
  def get_height (self): 
    return self.get_height_helper(self.root)

  def get_height_helper(self,node): # Recursively get the greatest height of the binary tree
    if node is None:
        return 0
    else :
        lDepth = self.get_height_helper(node.lchild)
        rDepth = self.get_height_helper(node.rchild)
        if(lDepth > rDepth): # Compare height of left and right and return the higher
            return lDepth+1
        else:
            return rDepth+1

        

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
      if self.root is None:
          return 0
      left = self.num_nodes_helper(self.root.lchild,0) # number of nodes in the left
      right = self.num_nodes_helper(self.root.rchild,0) # number of nodes in the right
      return left+right+1 # Just could have simply called self.num_nodes_helper(self.root) but the statement was unclear

  def num_nodes_helper (self,node,count):
    if node is None:
        return count
    else:
        return self.num_nodes_helper(node.lchild ,self.num_nodes_helper(node.rchild, count+1)) # first compute rightest node first recursively and hand that over to the leftside


  def print_tree(self):
    self.print_tree_helper(self.root, 0)

  def print_tree_helper(self, aNode, space):
    if aNode != None:
        space += SPACE
        self.print_tree_helper(aNode.rchild, space)
        print()
        for i in range(SPACE, space):
            print(end = " ")
        print(aNode.data)
        self.print_tree_helper(aNode.lchild, space)

        
def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints
    Tree1 = Tree()
    for i in range(len(tree1_input)):
        Tree1.insert(tree1_input[i])
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints
    Tree2 = Tree()
    for i in range(len(tree2_input)):
        Tree2.insert(tree2_input[i])
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints
    Tree3 = Tree()
    for i in range(len(tree3_input)):
        Tree3.insert(tree3_input[i])

if __name__ == "__main__":
  main()