"""
Write a function that accepts an array and a vlaue.
If the value is in the array then return the index of the value.
Else return -1.
"""


#O(n)
def linear_search(array,value):
    for index,item in enumerate(array):
        if item == value:
            return index
    else:
        return -1


#demo
print(linear_search([1,2,3],3))
print(linear_search([1,2,3],4))