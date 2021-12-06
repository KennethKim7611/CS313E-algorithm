#  File: DNA.py

#  Description:Finds the longest common dna sequence

#  Student Name: Kenneth Kim

#  Student UT EID: KK34556

#  Partner Name: Bruce Kim

#  Partner UT EID: bsk674

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 1/22/2021

#  Date Last Modified: 1/23/2021

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.

import sys

def longest_subsequence (s1, s2):
    res = list()
    # set: use a set for extra credit
    # res = set()
    max_len = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            temp_s1 = i
            temp_s2 = j
            count = 0

            # Explore from s1[i] and s2[j] to determine max substring
            while temp_s1 < len(s1) and temp_s2 < len(s2) and s1[temp_s1] == s2[temp_s2]:
                temp_s1 += 1
                temp_s2 += 1
                count += 1

            if count > max_len:
                #new max_len, clear res list and add substring
                max_len = count
                res.clear()
                res.append(s1[i:temp_s1])
                # extra credit: set uses add instead of append
                # res.clear()
                # res.add(s1[i:temp_s1])
            elif max_len != 0 and count == max_len:
                #equivalent length, add to res
                res.append(s1[i:temp_s1])
                # extra credit
                # res.add(s1[i:temp_s1])
    return res

def main():
    # read the data
    num = int(sys.stdin.readline().strip())

    # for each pair
    for i in range(num):
        s1 = sys.stdin.readline().strip()
        s2 = sys.stdin.readline().strip()

        result = longest_subsequence(s1, s2)

        if len(result) == 0:
            print('No Common Sequence Found')
        else:
            result.sort()
            # extra credit
            # result = sorted(result)
            for sequence in result:
                print(sequence)
            
        if i != num - 1:
            print()

if __name__ == "__main__":
    main()