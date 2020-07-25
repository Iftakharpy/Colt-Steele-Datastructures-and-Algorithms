"""
Write a recursive function that takes a number.
This function should add up all the numbers and return the sum.

Example:
1. sum_range(0) # 0
2. sum_range(1) # 1
3. sum_range(2) # 3
4. sum_range(3) # 6
5. sum_range(-1) # -1
6. sum_range(-4) # -10
"""

#O(n)
def sum_range(number):
    if number==0:
        return 0
    elif number>0:
        return number + sum_range(number-1)
    else:
        return number + sum_range(number+1)



#demo
print(sum_range(0)) # 0
print(sum_range(1)) # 1
print(sum_range(2)) # 3
print(sum_range(3)) # 6
print(sum_range(-1)) # -1
print(sum_range(-4)) # -10