"""
# Problem Pattern: Divide and Conquer

Problem Statement
-----------------
Write a function that called search which accepts a sorted array and a number.
Function should return the index of the number.
If the number is not in the array it should return None/undefined

Examples:
1. search([1,2,3,4,5,6,7,8,9,10],5) #4
1. search([1,2,3,4,5,6,7,8,9,10],0) #None
1. search([1,2,3,4,5,6,7,8,9,10],10) #9
1. search([1,2,3,4,5,6,7,8,9,10],2) #1
"""

def mid(low,high):
    return (low+high)//2

def search(arr,num):
    min_index = 0
    max_index = len(arr)-1
    while min_index<=max_index:
        mid_index = mid(min_index,max_index)
        if num>arr[mid_index]:
            min_index = mid_index+1
        elif num<arr[mid_index]:
            max_index = mid_index-1
        else:
            return mid_index
    return None


print(search([1,2,3,4,5,6,7,8,9,10],5)) #4
print(search([1,2,3,4,5,6,7,8,9,10],0)) #None
print(search([1,2,3,4,5,6,7,8,9,10],10)) #9
print(search([1,2,3,4,5,6,7,8,9,10],2)) #1