#O(n^2)
def selection_sort(array):
    for i in range(len(array)):
        index_of_min_value = i
        for j in range(i+1,len(array)):
            if array[j]<array[index_of_min_value]:
                index_of_min_value = j

        #swap
        array[i],array[index_of_min_value] = array[index_of_min_value],array[i]
    return array

print(selection_sort([3,2,5,1,5,6,0,72,2]))