"""
Write a recursive function that takes a number.
This function should return factorial of the number.
If the number is negative this function should return None

Example:
1. factorial(1) #1
2. factorial(2) #2
3. factorial(3) #6
4. factorial(4) #24
5. factorial(0) #1
6. factorial(-1) #None
7. factorial(-100) #None
"""

#O(n)
def factorial(number):
    if number>=0 and number<=1:
        return 1
    elif number<0:
        return None
    else:
        return number*factorial(number-1)



#demo
print(factorial(1)) #1
print(factorial(2)) #2
print(factorial(3)) #6
print(factorial(4)) #24
print(factorial(0)) #1
print(factorial(-1)) #None
print(factorial(-100)) #None