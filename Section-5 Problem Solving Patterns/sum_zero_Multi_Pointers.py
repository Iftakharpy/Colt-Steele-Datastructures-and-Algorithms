"""
# Problem Pattern: Mulitple Pointers

Problem Statement
-----------------
Write a function called sum_zero which accepts a sorted array of integers.
The function should find the first pair where sum is 0.
Return an array/tuple that includes both vallues that sum to zero or None/undefined if a pair does not exist.

Examples:
1. sum_zero([1,2,3]) # None
2. sum_zero([-1,0,1,2,3]) # [-1,1]
3. sum_zero([-2,-1,0,1,2,3]) # [-2,2]
4. sum_zero([-4,1,2,3,4,5,6,7,8]) # [-4,4]
"""

#O(n)
def sum_zero(lst):
    left_pointer = 0
    right_pointer = len(lst)-1

    while not left_pointer==right_pointer:
        sum = lst[left_pointer] + lst[right_pointer]
        if sum == 0:
            return [lst[left_pointer],lst[right_pointer]]
        elif sum > 0:
            right_pointer -= 1
        else:
            left_pointer += 1
    return None


#O(n^2)
def naive_sum_zero(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==0:
                return [lst[i],lst[j]]
    return None

print(naive_sum_zero([1,2,3])) # None
print(naive_sum_zero([-1,0,1,2,3])) # [-1,1]
print(naive_sum_zero([-2,-1,0,1,2,3])) # [-2,2]
print(naive_sum_zero([-4,1,2,3,4,5,6,7,8])) # [-4,4]