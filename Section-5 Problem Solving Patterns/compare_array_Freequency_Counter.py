"""
# Problem Pattern: Freequency Counter

Problem Statement
-----------------
Write a function called Same, which acepts two arrays.
And returns if every value in the first array has it's corresponding value squared in the second array.
The frequency of values must be the same.

Examples:
1. Same([1,2,3], [1,4,9]) #True
2. Same([2,1,3], [9,4,1]) #True
3. Same([2,3], [1,4,9]) #False
4. Same([1,2,4], [1,4,9]) #False
5. Same([1,2,1], [4,4,1]) #False
"""


#O(n^3)
def naive_Same(list1, list2):
    if len(list1)!=len(list2):
        return False
    for num in list1: #O(n)
        num=num**2
        if num in list2: #O(n)
            list2.remove(num) #O(n)
        else:
            return False
    return True


#O(n+m) -> O(n)
def fairly_good_Same(list1, list2):
    if len(list1)!=len(list2):
        return False

    lookup_table = {}
    for item in list2: #O(n)
        if lookup_table.get(item): #O(1)
            lookup_table[item]+=1 
        else:
            lookup_table[item]=1

    for num in list1: #O(m)
        num = num**2
        if lookup_table.get(num): #O(1)
            lookup_table[num]-=1
        else:
            return False
    return True

