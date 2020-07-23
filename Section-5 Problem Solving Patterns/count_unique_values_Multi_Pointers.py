"""
# Problem Pattern: Multi Pointers

Problem Statement
-----------------
Write a fuction which accepts a sorted array. And counts number of unique values in a given sorted array.

Examples:
1. count_unique_values([-1,0,1,2,3,4]) #6
2. count_unique_values([]) #0
2. count_unique_values([1,1,1,2]) #2
"""


# O(n)
# Using extra memory/space
def count_unique_values(lst):
    unique_values = 0
    lookup = {}
    for item in lst: #O(n)
        if lookup.get(item):
            continue
        else:
            unique_values+=1
            lookup[item]=True

    return unique_values

#O(n)
# Without using any extra memory/space
def count_unique_values(lst):
    if not lst:
        return 0
    count=1
    i=0
    for j in range(1,len(lst)): #O(n)
        if lst[i]!=lst[j]:
            count+=1
            i=j
    return count