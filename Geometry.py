#  File: Geometry.py
 
#  Description: Given Coordinate and adimtional infor compute multiple tasks
 
#  Student Name: Kenneth Kim

#  Student UT EID: KK34556

#  Partner Name: Bruce Kim

#  Partner UT EID: bsk674

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 2/12/2021

#  Date Last Modified: 2/13/2021
 
import math,sys
 
 
class Point (object):
 def __init__ (self, x = 0, y = 0, z = 0):
   self.x = x
   self.y = y
   self.z = z
 
 def __str__ (self):
   return ('({}, {}, {})'.format(float(self.x), float(self.y), float(self.z)))
 
 def distance (self, other):
   return float(math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 \
     + (self.z - other.z) ** 2))
 
 def __eq__ (self, other):
   tol = 1.0e-6
   return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) \
     and (abs(self.z - other.z) < tol))
 
 
 
class Sphere (object):
 def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
   self.x = x
   self.y = y
   self.z = z
   self.radius = radius
   self.center=Point(self.x,self.y,self.z)
 
 def __str__ (self):
   return ('Center: ({}, {}, {}), Radius: {}'.format(float(self.x), float(self.y), float(self.z), \
     float(self.radius)))
 
 def area (self):
   return float(4 * math.pi * (self.radius ** 2))
 
 def volume (self):
   return float((4 / 3) * math.pi *(self.radius ** 3))
 
 def is_inside_point (self, p):
   return self.radius > (math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2 \
     + (self.z - p.z) ** 2))
 
 def is_inside_sphere (self, other):
   return self.radius > ((math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 \
     + (self.z - other.z) ** 2)) + other.radius)
 
 def is_inside_cube (self, a_cube):
   corners = []
   corners.append(Point(a_cube.x + a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z + a_cube.side/2))
   corners.append(Point(a_cube.x + a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z - a_cube.side/2))
   corners.append(Point(a_cube.x + a_cube.side/2, a_cube.y - a_cube.side/2, a_cube.z + a_cube.side/2))
   corners.append(Point(a_cube.x + a_cube.side/2, a_cube.y - a_cube.side/2, a_cube.z - a_cube.side/2))
   corners.append(Point(a_cube.x - a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z + a_cube.side/2))
   corners.append(Point(a_cube.x - a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z - a_cube.side/2))
   corners.append(Point(a_cube.x - a_cube.side/2, a_cube.y - a_cube.side/2, a_cube.z + a_cube.side/2))
   corners.append(Point(a_cube.x - a_cube.side/2, a_cube.y - a_cube.side/2, a_cube.z - a_cube.side/2))
   for corner in corners:
      if Sphere.is_inside_point(self,corner):
        continue
      else:
        return False
   return True
 
 def is_inside_cyl (self, a_cyl):
   corners = []
   corners.append(Point(a_cyl.x + a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z + a_cyl.height/2))
   corners.append(Point(a_cyl.x + a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z - a_cyl.height/2))
   corners.append(Point(a_cyl.x + a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z + a_cyl.height/2))
   corners.append(Point(a_cyl.x + a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z - a_cyl.height/2))
   corners.append(Point(a_cyl.x - a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z + a_cyl.height/2))
   corners.append(Point(a_cyl.x - a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z - a_cyl.height/2))
   corners.append(Point(a_cyl.x - a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z + a_cyl.height/2))
   corners.append(Point(a_cyl.x - a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z - a_cyl.height/2))
 
   for corner in corners:
       if Sphere.is_inside_point(self, corner):
           continue
       else:
           return False
   return True
 
 def does_intersect_sphere (self, other):
   distance_centers = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
   return self.radius + other.radius >= distance_centers >= abs(self.radius - other.radius)
  
 # determine if a Cube intersects this Sphere
 # the Cube and Sphere intersect if they are not strictly inside or not strictly outside the other
 # a_cube is a Cube object
 # returns a Boolean
 def does_intersect_cube (self, a_cube):
    if not Sphere.is_inside_cube(self, a_cube):
      corners = []
      corners.append(Point(a_cube.x + a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z + a_cube.side/2))
      corners.append(Point(a_cube.x + a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z - a_cube.side/2))
      corners.append(Point(a_cube.x + a_cube.side/2, a_cube.y - a_cube.side/2, a_cube.z + a_cube.side/2))
      corners.append(Point(a_cube.x + a_cube.side/2, a_cube.y - a_cube.side/2, a_cube.z - a_cube.side/2))
      corners.append(Point(a_cube.x - a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z + a_cube.side/2))
      corners.append(Point(a_cube.x - a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z - a_cube.side/2))
      corners.append(Point(a_cube.x - a_cube.side/2, a_cube.y - a_cube.side/2, a_cube.z + a_cube.side/2))
      corners.append(Point(a_cube.x - a_cube.side/2, a_cube.y - a_cube.side/2, a_cube.z - a_cube.side/2))
      for corner in corners:
          if Sphere.is_inside_point(self, corner):
              return True
    return False
 
 def circumscribe_cube (self):
   return Cube(self.x, self.y, self.z, (2 / math.sqrt(3)) * self.radius)
 
 
 
 
class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.x=x
    self.y=y
    self.z=z
    self.side=side
    self.center=Point(self.x,self.y,self.z)
  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return ('Center: ({}, {}, {}), Side: {}'.format(float(self.x), float(self.y), float(self.z), float(self.side)))
  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return self.side**2*6
  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return self.side**3
  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    x_min = self.x - self.side/2
    x_max = self.x + self.side/2
    y_min = self.y - self.side/2
    y_max = self.y + self.side/2
    z_min = self.z - self.side/2
    z_max = self.z + self.side/2
    return (x_min < p.x < x_max and y_min < p.y < y_max  and z_min < p.z < z_max)
 
  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    corners = []
    corners.append(Point(a_sphere.x + a_sphere.radius, a_sphere.y + a_sphere.radius, a_sphere.z + a_sphere.radius))
    corners.append(Point(a_sphere.x + a_sphere.radius, a_sphere.y + a_sphere.radius, a_sphere.z - a_sphere.radius))
    corners.append(Point(a_sphere.x + a_sphere.radius, a_sphere.y - a_sphere.radius, a_sphere.z + a_sphere.radius))      
    corners.append(Point(a_sphere.x + a_sphere.radius, a_sphere.y - a_sphere.radius, a_sphere.z - a_sphere.radius))
    corners.append(Point(a_sphere.x - a_sphere.radius, a_sphere.y + a_sphere.radius, a_sphere.z + a_sphere.radius))
    corners.append(Point(a_sphere.x - a_sphere.radius, a_sphere.y + a_sphere.radius, a_sphere.z - a_sphere.radius))
    corners.append(Point(a_sphere.x - a_sphere.radius, a_sphere.y - a_sphere.radius, a_sphere.z + a_sphere.radius))     
    corners.append(Point(a_sphere.x - a_sphere.radius, a_sphere.y - a_sphere.radius, a_sphere.z - a_sphere.radius))
    for corner in corners:
        if Cube.is_inside_point(self, corner):
            continue
        else:
            return False
    return True
 
  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    corners = []
    corners.append(Point(other.x + other.side/2, other.y + other.side/2, other.z + other.side/2))
    corners.append(Point(other.x + other.side/2, other.y + other.side/2, other.z - other.side/2))
    corners.append(Point(other.x + other.side/2, other.y - other.side/2, other.z + other.side/2))
    corners.append(Point(other.x + other.side/2, other.y - other.side/2, other.z - other.side/2))
    corners.append(Point(other.x - other.side/2, other.y + other.side/2, other.z + other.side/2))
    corners.append(Point(other.x - other.side/2, other.y + other.side/2, other.z - other.side/2))
    corners.append(Point(other.x - other.side/2, other.y - other.side/2, other.z + other.side/2))
    corners.append(Point(other.x - other.side/2, other.y - other.side/2, other.z - other.side/2))
    for corner in corners:
        if Cube.is_inside_point(self, corner):
            continue
        else:
            return False
    return True
  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
    corners = []
    corners.append(Point(a_cyl.x + a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z + a_cyl.height/2))
    corners.append(Point(a_cyl.x + a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z - a_cyl.height/2))
    corners.append(Point(a_cyl.x + a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z + a_cyl.height/2))
    corners.append(Point(a_cyl.x + a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z - a_cyl.height/2))
    corners.append(Point(a_cyl.x - a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z + a_cyl.height/2))
    corners.append(Point(a_cyl.x - a_cyl.radius, a_cyl.y + a_cyl.radius, a_cyl.z - a_cyl.height/2))
    corners.append(Point(a_cyl.x - a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z + a_cyl.height/2))
    corners.append(Point(a_cyl.x - a_cyl.radius, a_cyl.y - a_cyl.radius, a_cyl.z - a_cyl.height/2))
    for corner in corners:
        if Cube.is_inside_point(self, corner):
            continue
        else:
            return False
    return True
  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    if not Cube.is_inside_cube(self, other):
      corners = []
      corners.append(Point(other.x + other.side/2, other.y + other.side/2, other.z + other.side/2))
      corners.append(Point(other.x + other.side/2, other.y + other.side/2, other.z - other.side/2))
      corners.append(Point(other.x + other.side/2, other.y - other.side/2, other.z + other.side/2))
      corners.append(Point(other.x + other.side/2, other.y - other.side/2, other.z - other.side/2))
      corners.append(Point(other.x - other.side/2, other.y + other.side/2, other.z + other.side/2))
      corners.append(Point(other.x - other.side/2, other.y + other.side/2, other.z - other.side/2))
      corners.append(Point(other.x - other.side/2, other.y - other.side/2, other.z + other.side/2))
      corners.append(Point(other.x - other.side/2, other.y - other.side/2, other.z - other.side/2))
      for corner in corners:
          if Cube.is_inside_point(self, corner):
              return True
    return False
          
  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    if Cube.does_intersect_cube(self,other):
      cube1_x_min = self.x-self.side/2
      cube1_x_max = self.x+self.side/2
      cube1_y_min = self.y-self.side/2
      cube1_y_max = self.y+self.side/2
      cube1_z_min = self.z-self.side/2
      cube1_z_max = self.z+self.side/2
      cube2_x_min = other.x-other.side/2
      cube2_x_max = other.x+other.side/2
      cube2_y_min = other.y-other.side/2
      cube2_y_max = other.y+other.side/2
      cube2_z_min = other.z-other.side/2
      cube2_z_max = other.z+other.side/2
      return float(max(min(cube2_x_max,cube1_x_max)-max(cube2_x_min,cube1_x_min),0)*max(min(cube2_y_max,cube1_y_max)-max(cube2_y_min,cube1_y_min),0)*max(min(cube2_z_max,cube1_z_max)-max(cube2_z_min,cube1_z_min),0))
    return 0
  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    return Sphere(self.x,self.y,self.z,self.side/2)
 
class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      self.x=x
      self.y=y
      self.z=z
      self.radius=radius
      self.height=height
      self.center=Point(self.x,self.y,self.z)
 
  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
      return 'Center: ({}, {}, {}), Radius: {}, Height: {}'.format(float(self.x),float(self.y),float(self.z),float(self.radius),float(self.height))
  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
      return math.pi*self.radius*2*self.height+2*math.pi*self.radius**2
  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
      return math.pi*self.radius**2*self.height
 
  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    x_min = self.x - self.radius
    x_max = self.x + self.radius
    y_min = self.y - self.radius
    y_max = self.y + self.radius
    z_min = self.z - self.height/2
    z_max = self.z + self.height/2
    return (x_min < p.x < x_max and y_min < p.y < y_max  and z_min < p.z < z_max)
    #return (math.sqrt((p.x-self.x)**2+(p.y-self.y)**2)<self.radius and self.z-self.height/2<p.z<self.z+self.height/2)
 
  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    if Cylinder.is_inside_point(self, Point(a_sphere.x,a_sphere.y,a_sphere.z)):
      if self.radius>a_sphere.radius:
        if self.height>a_sphere.radius*2:
          return True
    return False
  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    if Cylinder.is_inside_point(self, Point(a_cube.x,a_cube.y,a_cube.z)):
      if (self.y-self.height/2<a_cube.y-a_cube.side/2 and self.y+self.height/2>a_cube.y+a_cube.side/2):
        corners = []
        corners.append(Point(a_cube.x + a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z + a_cube.side/2))
        corners.append(Point(a_cube.x + a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z - a_cube.side/2))
        corners.append(Point(a_cube.x - a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z + a_cube.side/2))
        corners.append(Point(a_cube.x - a_cube.side/2, a_cube.y + a_cube.side/2, a_cube.z - a_cube.side/2))      
        for corner in corners:
            if Cylinder.is_inside_point(self, corner):
                continue
            else:
                return False
        return True
    return False
        
  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    if Cylinder.is_inside_point(self, Point(other.x,other.y,other.z)):
      if self.radius>other.radius:
        if self.height>other.height:
          corners = []
          corners.append(Point(other.x + other.radius, other.y, other.z))
          corners.append(Point(other.x - other.radius, other.y, other.z))
          corners.append(Point(other.x, other.y, other.z + other.radius))
          corners.append(Point(other.x, other.y, other.z - other.radius))      
          for corner in corners:
              if Cylinder.is_inside_point(self, corner):
                  continue
              else:
                  return False
          return True
    return False
          
 
  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
    if not Cylinder.is_inside_cylinder(self,other):
      corners = []
      corners.append(Point(other.x + other.radius, other.y + other.radius, other.z + other.height/2))
      corners.append(Point(other.x + other.radius, other.y + other.radius, other.z - other.height/2))
      corners.append(Point(other.x + other.radius, other.y - other.radius, other.z + other.height/2))
      corners.append(Point(other.x + other.radius, other.y - other.radius, other.z - other.height/2))
      corners.append(Point(other.x - other.radius, other.y + other.radius, other.z + other.height/2))
      corners.append(Point(other.x - other.radius, other.y + other.radius, other.z - other.height/2))
      corners.append(Point(other.x - other.radius, other.y - other.radius, other.z + other.height/2))
      corners.append(Point(other.x - other.radius, other.y - other.radius, other.z - other.height/2))
      for corner in corners:
          if Cylinder.is_inside_point(self, corner):
              return False
    return True
      
def main():
  # read data from standard input
  # read the coordinates of the first Point p
  p = sys.stdin.readline().strip()
  coord = p.split(" ")
  # create a Point object 
  point1 = Point(float(coord[0]),float(coord[1]),float(coord[2]))
  # read the coordinates of the second Point q
  p = sys.stdin.readline().strip()
  coord = p.split(" ")
  # create a Point object 
  point2 = Point(float(coord[0]),float(coord[1]),float(coord[2]))
  # read the coordinates of the center and radius of sphereA
  p = sys.stdin.readline().strip()
  coord = p.split(" ")
  # create a Sphere object 
  sphere1 = Sphere(float(coord[0]),float(coord[1]),float(coord[2]),float(coord[3]))
  # read the float(coordinates of the center and radius of sphereB
  p = sys.stdin.readline().strip()
  coord = p.split(" ")
  # create a Sphere object
  sphere2 = Sphere(float(coord[0]),float(coord[1]),float(coord[2]),float(coord[3]))
  # read the coordinates of the center and side of cubeA
  p = sys.stdin.readline().strip()
  coord = p.split(" ")
  # create a Cube object 
  cube1 = Cube(float(coord[0]),float(coord[1]),float(coord[2]),float(coord[3]))
  # read the coordinates of the center and side of cubeB
  p = sys.stdin.readline().strip()
  coord = p.split(" ")
  # create a Cube object 
  cube2 = Cube(float(coord[0]),float(coord[1]),float(coord[2]),float(coord[3]))
  # read the coordinates of the center, radius and height of cylA
  p = sys.stdin.readline().strip()
  coord = p.split(" ")
  # create a Cylinder object 
  cylinder1 = Cylinder(float(coord[0]),float(coord[1]),float(coord[2]),float(coord[3]),float(coord[4]))
  # read the coordinates of the center, radius and height of cylB
  p = sys.stdin.readline().strip()
  coord = p.split(" ")
  # create a Cylinder object
  cylinder2 = Cylinder(float(coord[0]),float(coord[1]),float(coord[2]),float(coord[3]),float(coord[4]))
  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
  origin = Point(0,0,0)
  print("Distance of Point p from the origin"+(" is " if point1.distance(origin)>point2.distance(origin) else " is not ")+"greater than the distance of Point q from the origin")
  # print if Point p is inside sphereA
  print("Point p"+(" is " if sphere1.is_inside_point(point1) else " is not ")+"inside sphereA")
  # print if sphereB is inside sphereA
  print("sphereB"+(" is " if sphere1.is_inside_sphere(sphere2) else " is not ")+"inside sphereA")
  # print if cubeA is inside sphereA
  print("cubeA"+(" is " if sphere1.is_inside_cube(cube1) else " is not ")+"inside sphereA")
  # print if cylA is inside sphereA
  print("cylA"+(" is " if sphere1.is_inside_cyl(cylinder1) else " is not ")+"inside sphereA")
  # print if sphereA intersects with sphereB
  print("sphereA"+(" does " if sphere1.does_intersect_sphere(sphere2) else " does not ")+"intersect sphereB")
  # print if cubeB intersects with sphereB
  print("cubeB"+(" does " if sphere2.does_intersect_cube(cube2) else " does not ")+"intersect sphereB")
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  print("Volume of the largest Cube that is circumscribed by sphereA"+(" is " if Cube.volume(sphere1.circumscribe_cube())>cylinder1.volume() else " is not ")+"greater than the volume of cylA")
  # print if Point p is inside cubeA
  print("Point p"+(" is " if cube1.is_inside_point(point1) else " is not ")+"inside cubeA")
  # print if sphereA is inside cubeA
  print("sphereA"+(" is " if sphere1.is_inside_cube(cube1) else " is not ")+"inside cubeA")
  # print if cubeB is inside cubeA
  print("cubeB"+(" is " if cube1.is_inside_cube(cube2) else " is not ")+"inside cubeA")
  # print if cylA is inside cubeA
  print("cylA"+(" is " if cube1.is_inside_cylinder(cylinder1) else " is not ")+"inside cubeA")
  # print if cubeA intersects with cubeB
  print("cubeA"+(" does " if cube1.does_intersect_cube(cube2) else " does not ")+"intersect cubeB")
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  print("Intersection volume of cubeA and cubeB"+(" is " if  cube1.intersection_volume(cube2)  > sphere1.volume() else " is not ")+"greater than the volume of sphereA")
  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  print("Surface area of the largest Sphere object inscribed by cubeA"+(" is " if  Sphere.area(cube1.inscribe_sphere())> cylinder1.area() else " is not ")+"greater than the surface area of cylA")
  # print if Point p is inside cylA
  print("Point p"+(" is " if cylinder1.is_inside_point(point1) else " is not ")+"inside cylA")
  # print if sphereA is inside cylA
  print("sphereA"+(" is " if cylinder1.is_inside_sphere(sphere1) else " is not ")+"inside cylA")
  # print if cubeA is inside cylA
  print("cubeA"+(" is " if cylinder1.is_inside_cube(cube1) else " is not ")+"inside cylA")
  # print if cylB is inside cylA
  print("cylB"+(" is " if cylinder1.is_inside_cylinder(cylinder1) else " is not ")+"inside cylA")
  # print if cylB intersects with cylA
  print("cylB"+(" does not " if cylinder1.does_intersect_cylinder(cylinder2) else " does ")+"intersect cylA")
 
if __name__ == "__main__":
  main()
 
 