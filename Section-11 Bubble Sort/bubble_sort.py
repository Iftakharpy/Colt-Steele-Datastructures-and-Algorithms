#inplace sort
#O(n^2)
def bubble_sort(array): #Unoptimized
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j]>array[j+1]:
                #swap
                array[j],array[j+1] = array[j+1],array[j]
    return array


#inplace sort
#optimized but still O(n^2)
def optimized_bubble_sort(array):
    for i in range(len(array),0,-1):
        not_swaped = True
        for j in range(i-1):
            if array[j]>array[j+1]:
                #swap
                array[j],array[j+1] = array[j+1],array[j]
                not_swaped = False
        if not_swaped:
            break
    return array



#demo
# import random

# test_arr = [random.randint(0,1000) for i in range(1000)]

# print(test_arr)
# print(optimized_bubble_sort(test_arr))
# print(test_arr)


print(optimized_bubble_sort([4,2,5,1,5,1,6,7,8,9,3,0,10]))
