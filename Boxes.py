
#  File: Boxes.py

#  Description: Calculates max number of boxes nested; and the number of such

#  Student Name: Kenneth Kim

#  Student UT EID: KK34556

#  Partner Name: Bruce Kim

#  Partner UT EID:bsk674

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 3/24/2021

#  Date Last Modified: 3/24/2021

import sys

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes

def sub_sets_boxes(box_list, sub_set, idx, all_box_subsets):
 if len(all_box_subsets) >= 2 ** len(box_list):
   return all_box_subsets
 elif (idx == len(box_list)):
   all_box_subsets.append(sub_set)
 else:
   c = sub_set[:]
   sub_set.append(box_list[idx])
   sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
   sub_sets_boxes(box_list, c, idx + 1, all_box_subsets)
#creates all_box_subsets, which is permutation of box_list, through recursion

def largest_nesting_subsets (all_box_subsets):
  fit = []
  for i in range(len(all_box_subsets)-1):
    check = True
    for j in range(len(all_box_subsets[i])-1):
      if not does_fit(all_box_subsets[i][j],all_box_subsets[i][j+1]):
        check = False
    if check:
      fit.append(all_box_subsets[i])
  #To check if given list inside list is possible box nest combination    
  max=0
  temp=[]
  for i in range(len(fit)):
    if max<len(fit[i]):
      max=len(fit[i])
  for i in range(len(fit)):
    if max==len(fit[i]):
      temp.append(fit[i])
  #Loop through fit[] to find max box nested list
  return temp




# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  '''
  # print to make sure that the input was read in correctly
  print (box_list)
  print()
  '''

  # sort the box list
  box_list.sort()

  '''
  #print the box_list to see if it has been sorted.
  print (box_list)
  print()
  '''

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes(box_list, sub_set, 0, all_box_subsets)
  # all_box_subsets should have a length of 2^n where n is the number
  # of boxes

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  all_nesting_boxes = largest_nesting_subsets (all_box_subsets)

  # print the largest number of boxes that fit
  print(len(all_nesting_boxes[0]))
  # print the number of sets of such boxes
  print(len(all_nesting_boxes))

if __name__ == "__main__":
  main()
