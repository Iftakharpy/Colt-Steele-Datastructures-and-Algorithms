"""
# Problem Pattern: Freequency Counter

Problem Statement
-----------------
Write a function called same_frequency, which acepts two arrays.
Which should return True if the frequency of the elements in the arrays for every element is same.
Else this should return False.

Examples:
1. same_frequency([1,2,5,1,3],[1,2,1,5,3]) #True
2. same_frequency([1,2],[2,1]) #True
3. same_frequency([1,2,6,5],[5,1,2,6]) #True
4. same_frequency([1,2,5,1,3],[1,2,1,5,3,4]) #False
5. same_frequency([1,2,5,1,3],[1,2]) #False
"""


# O(n+k)
def same_frequency(lst1,lst2):
    lookup = {}
    for num in lst1:
        if not lookup.get(num):
            lookup[num]=1
        else:
            lookup[num]+=1
    lookup2 = {}
    for num in lst2:
        if not lookup2.get(num):
            lookup2[num]=1
        else:
            lookup2[num]+=1
    if not lookup==lookup2:
        return False
    return True


print(same_frequency([1,2,5,1,3],[1,2,1,5,3])) #True
print(same_frequency([1,2],[2,1])) #True
print(same_frequency([1,2,6,5],[5,1,2,6])) #True
print(same_frequency([1,2,5,1,3],[1,2,1,5,3,4])) #False
print(same_frequency([1,2,5,1,3],[1,2])) #False