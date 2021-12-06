# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name: Kenneth Kim

# Student UT EID: KK34556

# Course Name: CS 313E

# Unique Number:

import sys
import math

TOL = 0.01

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

class Triangle (object):
    # constructor
    # TODO: YOUR CODE HERE
    def __init__ (self, Point1, Point2, Point3):
      self.Point1 = Point1
      self.Point2 = Point2
      self.Point3 = Point3
      self.area = Triangle.area(self)

    # print string representation of Triangle
    # TODO: YOUR CODE HERE
    def __str__ (self):
      return ("Point1: ({}, {}), Point2: ({}, {}), Point3: ({}, {}), Area: {}".format(self.Point1.x,self.Point1.y,self.Point2.x,self.Point2.y,self.Point3.x,self.Point3.y,self.area))

    # check congruence of Triangles with equality
    # TODO: YOUR CODE HERE
    def __eq__(self, other):
      a = Point.dist(self.Point1,self.Point2)
      b = Point.dist(self.Point2,self.Point3)
      c = Point.dist(self.Point3,self.Point1)
      lst = [a,b,c]
      lst.sort
      d = Point.dist(other.Point1,other.Point2)
      e = Point.dist(other.Point2,other.Point3)
      f = Point.dist(other.Point3,other.Point1)
      lst2 = [d,e,f]
      lst2.sort
      return lst==lst2


    # returns whether or not the triangle is valid
    # TODO: YOUR CODE HERE
    def is_triangle(self):
      a = Point.dist(self.Point1,self.Point2)
      b = Point.dist(self.Point2,self.Point3)
      c = Point.dist(self.Point3,self.Point1)
      if (a+b>=c+TOL and b+c>=a+TOL) and c+a>=b+TOL:
        return True
      else:
        return False
    # return the area of the triangle:
    # TODO: YOUR CODE HERE
    def area(self):
      return abs(0.5*((self.Point1.x*(self.Point2.y-self.Point3.y))+(self.Point2.x*(self.Point3.y-self.Point1.y))+(self.Point3.x*(self.Point1.y-self.Point2.y))))

######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA)
    print(triangleB)
    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)

if __name__ == "__main__":
    main()
