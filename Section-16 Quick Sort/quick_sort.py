def pivot(array, start_index=0, end_index=-1):
    """
    Accepts an array and start index and end index.\n
    Pics first index's value as pivot and places it in the corrent place.\n
    Returns the index of the pivot.
    """
    if end_index == -1:
        end_index = len(array)-1
    pivot_value = array[start_index]
    pivot_index = start_index

    numbers_smaller_than_pivot = 0
    while start_index<end_index:
        start_index += 1
        if array[start_index] <= pivot_value:
            numbers_smaller_than_pivot+=1
            array[start_index],array[pivot_index+numbers_smaller_than_pivot] = array[pivot_index+numbers_smaller_than_pivot],array[start_index]
    array[pivot_index], array[pivot_index+numbers_smaller_than_pivot] = array[pivot_index+numbers_smaller_than_pivot], array[pivot_index]
    return pivot_index+numbers_smaller_than_pivot


def quick_sort(array,start=0,end=-1):
    if end==-1:
        end = len(array)-1
    
    #left sort
    if end-start>1:
        mid = pivot(array,start,end)
        # if mid+1>start:
        quick_sort(array,start,mid-1)

        #right sort
        # if mid+1<end:
        quick_sort(array,mid+1,end)

    return array




#test
import random
from copy import deepcopy

arr_len = 99999
tests = 100000
for i in range(tests):
    array = [random.randint(0,1000) for x in range(arr_len)]
    clone  = deepcopy(array)
    array.sort()
    print('sorted array')
    quick_sort(clone)
    print('sorted clone')
    print(array==clone,i)
    if array==clone:
        continue
    else:
        break