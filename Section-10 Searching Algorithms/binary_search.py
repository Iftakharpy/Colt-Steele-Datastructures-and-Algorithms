"""
Write a function that accepts a sorted array and a vlaue.
If the value is in the array then return the index of the value.
Else return -1.
"""


def mid(low,high):
    return (low+high)//2

#works only on sorted arrays
#O(logN)
def binary_search(array,value):
    low_index = 0
    high_index = len(array)-1
    mid_index = mid(low_index,high_index)

    while low_index != high_index:
        if value>array[mid_index]:
            low_index = mid_index+1
        elif value<array[mid_index]:
            high_index = mid_index-1
        else:
            break
        mid_index = mid(low_index,high_index)

    if array[mid_index]==value:
        return mid_index
    return -1


#demo
print(binary_search([1,2,3,4],10))
print(binary_search([1,2,3,4],2))
print(binary_search([1,2,3,4],3))
print(binary_search([1,2,3,4],4))
print(binary_search([1,2,3,4],1))