"""
# Problem Pattern: Freequency Counter/Multi Pointer

Problem Statement
-----------------
Write a function called are_there_duplicates, which acepts an array.
Which should return True if all elements are unique.
Else this should return False.

Examples:
1. are_there_duplicates([1,2,5,3]) #True
2. are_there_duplicates([1,2]) #True
3. are_there_duplicates([1,2,6,5]) #True
4. are_there_duplicates([0,0]) #False
5. are_there_duplicates([1,2,3,1]) #False
"""


#O(n)
def are_there_duplicates(arr):
    counter = {}
    for ele in arr:
        if counter.get(ele):
            return False
        counter[ele]=True
    return True


#O(NlogN)
def are_there_duplicates(arr):
    #Multi pointer solution
    arr.sort()
    start_ptr = 0
    next_ptr = 1
    while next_ptr < len(arr):
        if arr[start_ptr]==arr[next_ptr]:
            return False
        start_ptr += 1
        next_ptr += 1
    return True


#one_liner
#O(n)
def are_there_duplicates(arr):
    return len(arr)==len(set(arr))

