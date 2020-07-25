"""
Write a recursive function that takes an array which contains number.
This function should return product of these numbers.

Example:
1. product([1,3,5]) # 15
2. product([1,3,5,0]) # 0
3. product([-1,3,5]) # -15
4. product([-1]) # -1
5. product([3]) # 3
6. product([]) # None
"""


def product(numbers):
    if len(numbers)==1:
        return numbers[0]
    elif len(numbers)==0:
        return None
    else:
        return numbers.pop()*product(numbers)



#demo
print(product([1,3,5])) # 15
print(product([1,3,5,0])) # 0
print(product([-1,3,5])) # -15
print(product([-1])) # -1
print(product([3])) # 3
print(product([])) # None