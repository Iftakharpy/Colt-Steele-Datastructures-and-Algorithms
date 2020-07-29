#takes 2 sorted arrays and returns a sorted array by merging them together
#O(n+m)
def merge(array1,array2): # this function is a mess to read
    sorted_array = []

    array1_index = 0
    array1_limit = len(array1)-1

    array2_index = 0
    array2_limit = len(array2)-1

    while array1_index<=array1_limit or array2_index<=array2_limit:
        if len(array1)==0 or array1_index==len(array1):
            for i in range(array2_index,len(array2)):
                sorted_array.append(array2[i])
            break
        elif len(array2)==0 or array2_index==len(array2):
            for i in range(array1_index,len(array1)):
                sorted_array.append(array1[i])
            break
        else:
            if array1[array1_index]<array2[array2_index]:
                sorted_array.append(array1[array1_index])
                array1_index+=1
            else:
                sorted_array.append(array2[array2_index])
                array2_index+=1

    return sorted_array

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
def merge_sort(array):
    if len(array)<=1:
        return array

    mid_index = len(array)//2
    left_slice = merge_sort(array[:mid_index]) #O(log(n))
    right_slice = merge_sort(array[mid_index:]) #O(log(n))
    print(left_slice,right_slice)
    return merge(left_slice,right_slice) #O(n+m)


print(merge_sort([1,1,3,5,9,8,6,7,1,3,4]))