# Author: Bishal Sarang

# Import Visualiser class from module visualiser
from visualiser.visualiser import Visualiser as vs



#O(n+m)
def alternative_merge(array1,array2): #this function is easier to read
    merged_array=[]

    array1_index = 0
    array2_index = 0
    while array1_index<len(array1) and array2_index<len(array2):
        if array1[array1_index]<array2[array2_index]:
            merged_array.append(array1[array1_index])
            array1_index+=1
        else:
            merged_array.append(array2[array2_index])
            array2_index+=1

    #if we dodn't added numbers from one of the lists then add them to the merged list now
    while array1_index<len(array1):
        merged_array.append(array1[array1_index])
        array1_index+=1
    while array2_index<len(array2):
        merged_array.append(array2[array2_index])
        array2_index+=1

    #return the merged array
    return merged_array



#time complexity is O(nlog(n)) because we are recursively calling the merge_sort function n times
#where time complexity of the left_slice or right_slice is O(log(n))
#O(nlog(n)) - time
#space complexity is n because we are splitting the list in n smaller arrays
#O(n) - space
@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def merge_sort(array):
    if len(array)<=1:
        return array

    mid_index = len(array)//2
    left_slice = merge_sort(array[:mid_index]) #O(log(n))
    right_slice = merge_sort(array[mid_index:]) #O(log(n))
    return alternative_merge(left_slice,right_slice) #O(n+m)


def main():
    # Call function
    print(merge_sort([5,0,1,9]))
    # Save recursion tree to a file
    vs.make_animation("merge_sort.gif", delay=1.3)


if __name__ == "__main__":
    main()