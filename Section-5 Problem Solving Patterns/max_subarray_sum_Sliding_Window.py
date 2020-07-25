"""
# Problem Pattern: Sliding Window

Problem Statement
-----------------
Write a fuction that accepts a list and a number N.
The function should return the maximum sum of N consecutive numbers in the array.

Examples:
1. max_subarray_sum([1], 2) #None
2. max_subarray_sum([1, 3, 4, 2, 12, 3], 1) #12
3. max_subarray_sum([2, 3, 4, 5, 12, 4], 2) #17
4. max_subarray_sum([9, 2, 3, 1, 2, 10], 2) #12
"""


#O(n^2)
def naive_max_subarray_sum(lst, N):
    if len(lst)<N:
        return None

    max_sum = 0
    for i in range(len(lst)-N+1): #O(n)
        temp_sum = 0
        for j in range(i,i+N): #O(m)
            temp_sum += lst[j]
        if temp_sum>max_sum:
            max_sum=temp_sum
    return max_sum



#O(n)
def max_subarray_sum(lst, N):
    if len(lst)<N:
        return None
    max_sum = 0
    for i in range(N):
        max_sum += lst[i]
    
    temp_sum = max_sum
    for i in range(N,len(lst)):
        temp_sum = (temp_sum-lst[i-N]) + lst[i]
        max_sum = max(temp_sum,max_sum)
    return max_sum
