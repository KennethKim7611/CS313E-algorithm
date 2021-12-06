#  File: TopoSort.py
#  Description: Determine whether the graph has a circle, and if it does not have, do topo sort.
 
#  Student Name: Bruce Kim
#  Student UT EID: bsk674
#  Partner Name: Kenneth Kim
#  Partner UT EID: KK34556
#  Course Name: CS 313E
#  Unique Number:52240
#  Date Created: 05/02/21
#  Date Last Modified: 05/02/21
import sys
 
class Stack (object):
 def __init__ (self):
   self.stack = []
 
 # add an item to the top of the stack
 def push (self, item):
   self.stack.append (item)
 
 # remove an item from the top of the stack
 def pop (self):
   return self.stack.pop()
 
 # check the item on the top of the stack
 def peek (self):
   return self.stack[-1]
 
 # check if the stack if empty
 def is_empty (self):
   return (len (self.stack) == 0)
 
 # return the number of elements in the stack
 def size (self):
   return (len (self.stack))
 
 
class Queue (object):
 def __init__ (self):
   self.queue = []
 
 # add an item to the end of the queue
 def enqueue (self, item):
   self.queue.append (item)
 
 # remove an item from the beginning of the queue
 def dequeue (self):
   return (self.queue.pop(0))
 
 # check if the queue is empty
 def is_empty (self):
   return (len (self.queue) == 0)
 
 # return the size of the queue
 def size (self):
   return (len (self.queue))
 
 
class Vertex (object):
 def __init__ (self, label):
   self.label = label
   self.visited = False
 
 # determine if a vertex was visited
 def was_visited (self):
   return self.visited
 
 # determine the label of the vertex
 def get_label (self):
   return self.label
 
 # string representation of the vertex
 def __str__ (self):
   return str (self.label)
 
 
class Graph (object):
 def __init__ (self):
   self.Vertices = []
   self.adjMat = []
 
 # check if a vertex is already in the graph
 def has_vertex (self, label):
   nVert = len (self.Vertices)
   for i in range (nVert):
     if (label == (self.Vertices[i]).get_label()):
       return True
   return False
 
 # given the label get the index of a vertex
 def get_index (self, label):
   nVert = len (self.Vertices)
   for i in range (nVert):
     if (label == (self.Vertices[i]).get_label()):
       return i
   return -1
 
 # add a Vertex with a given label to the graph
 def add_vertex (self, label):
   if (self.has_vertex (label)):
     return
 
   # add vertex to the list of vertices
   self.Vertices.append (Vertex (label))
 
   # add a new column in the adjacency matrix
   nVert = len (self.Vertices)
   for i in range (nVert - 1):
     (self.adjMat[i]).append (0)
 
   # add a new row for the new vertex
   new_row = []
   for i in range (nVert):
     new_row.append (0)
   self.adjMat.append (new_row)
  # delete the vertex from the graph
 def delete_vertex (self, vertexLabel):
   vertex=self.get_index(vertexLabel)
   for i in range(len(self.adjMat)):
     del(self.adjMat[i][vertex])
   del(self.adjMat[vertex])
   del(self.Vertices[vertex])
 
 # add weighted directed edge to graph
 def add_directed_edge (self, start, finish, weight = 1):
   self.adjMat[start][finish] = weight
 
 # add weighted undirected edge to graph
 def add_undirected_edge (self, start, finish, weight = 1):
   self.adjMat[start][finish] = weight
   self.adjMat[finish][start] = weight
 
 # return an unvisited vertex adjacent to vertex v (index)
 def get_adj_unvisited_vertex (self, v):
   nVert = len (self.Vertices)
   for i in range (nVert):
     if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
       return i
   return -1
 
 def get_adj_vertices (self,v):
   nVert = len (self.Vertices)
   lst = []
   for i in range (nVert):
     if (self.adjMat[v][i] > 0) and ((self.Vertices[i]).was_visited()):
       lst.append(self.Vertices[i])
   return lst
 
 # do a depth first search in a graph
 def has_cycle (self):
   # create the Stack
   theStack = Stack ()
   visited_list = []
 
   for i in range(len(self.Vertices)):
     # if Vertices[i] is already visited, no need to check it again.
     if (self.Vertices[i]) in visited_list:
       continue
     else:
       (self.Vertices[i]).visited = True
       visited_list.append(self.Vertices[i])
       theStack.push (i)
 
       # visit all the other vertices according to depth
       while (not theStack.is_empty()):
         # find all visited adjacent vertices
         lst = self.get_adj_vertices(theStack.peek())
         for i in lst:
           # theStack.peek() is connected to the visited vertex, which means it forms a cycle.
           if i in visited_list:
             return True
         # get an adjacent unvisited vertex
         u = self.get_adj_unvisited_vertex(theStack.peek())
         if (u == -1):
           u = theStack.pop()
           visited_list.pop()
         else:
           (self.Vertices[u]).visited = True
           visited_list.append(self.Vertices[u])
           theStack.push(u)
   return False
 
   # the stack is empty, let us rest the flags
   nVert = len (self.Vertices)
   for i in range (nVert):
     (self.Vertices[i]).visited = False
 
 # return a list of vertices after a topological sort
 def toposort (self):
   temp = Graph()
   temp.Vertices=self.Vertices
   temp.adjMat=self.adjMat
   topo_visit = []
   delete_list = []
   idx = 0
   while(len(temp.Vertices) > 0):
     idx = 0
     while(idx < len(temp.Vertices)):
       has_visit = False
       vertex=temp.Vertices[idx].label
       for i in range(len(temp.Vertices)):
         if(temp.adjMat[i][idx] == 1):
           has_visit = True
           break
       if(has_visit):
         idx+=1
       else:
         topo_visit.append(vertex)
         delete_list.append(vertex)
         idx += 1
     while(len(delete_list)>0):
       temp.delete_vertex(delete_list[0])
       delete_list.pop(0)
   return topo_visit
 
def main():
 # create the Graph object
 cities = Graph()
 
 # read the number of vertices
 line = sys.stdin.readline()
 line = line.strip()
 num_vertices = int (line)
 
 # read the vertices to the list of Vertices
 for i in range (num_vertices):
   line = sys.stdin.readline()
   city = line.strip()
   cities.add_vertex (city)
 
 # read the number of edges
 line = sys.stdin.readline()
 line = line.strip()
 num_edges = int (line)
 
 # read each edge and place it in the adjacency matrix
 for i in range (num_edges):
   line = sys.stdin.readline()
   edge = line.strip()
   edge = edge.split()
   start = int (cities.get_index(edge[0]))
   finish = int (cities.get_index(edge[1]))
 
 
   cities.add_directed_edge (start, finish)
 
 # test if a directed graph has a cycle
 if (cities.has_cycle()):
   print ("The Graph has a cycle.")
 else:
   print ("The Graph does not have a cycle.")
   print ("\nList of vertices after toposort")
   print (cities.toposort())
 
main()
 
 
 

