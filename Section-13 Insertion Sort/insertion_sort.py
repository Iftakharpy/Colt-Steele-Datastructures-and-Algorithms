"""
This sorting algorithm is good at putting live data in the correct place.
Example: Let's say we want sorted list and we want to constantly add random numbers in that list.
         In this situation insertion_sort can come handy.
"""


#O(n^2)
def insertion_sort(array):
    for i in range(1,len(array)):
        #temp cache for current index value
        current_value = array[i]

        for j in range(i-1,-1,-1):
            #pushing the larger values to the right untill we find the right for the current_value
            if array[j]>current_value:
                array[j+1] = array[j]
            
            #stopping the loop if we find the right place
            if current_value>=array[j]:
                break
        
        #putting the number in the correct place
        array[j] = current_value
    return array



#demo
import random

arr = [random.randint(0,1000) for x in range(1000)]
print(arr.__sizeof__())
print(insertion_sort(arr))