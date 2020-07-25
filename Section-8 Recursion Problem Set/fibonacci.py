"""
Write a recursive function that takes a number.
This function should return N-th number of the fibonacci series.
If the number is negative this function should return None.

Example:
1. fibonacci(-1) # None
2. fibonacci(0) # 1
3. fibonacci(1) # 1
4. fibonacci(2) # 2
5. fibonacci(3) # 3
6. fibonacci(4) # 5
7. fibonacci(5) # 8
"""

# recursion without memoization
def fibonacci(number):
    if number<=-1:
        return None
    elif number<=1:
        return 1
    else:
        return fibonacci(number-2)+fibonacci(number-1)


# recursion with memoization
def memo_fibonacci(number,memo={}):
    if number<=-1:
        return None
    elif number<=1:
        return 1
    else:
        if memo.get(number):
            return memo[number]
        else:
            memo[number] = memo_fibonacci(number-2) + memo_fibonacci(number-1)
    return memo_fibonacci(number-2,memo) + memo_fibonacci(number-1,memo)



print(memo_fibonacci(1988))

"""
#demo
# print(fibonacci(-1)) # None
# print(fibonacci(0)) # 1
# print(fibonacci(1)) # 1
# print(fibonacci(2)) # 2
# print(fibonacci(3)) # 3
# print(fibonacci(4)) # 5
# print(fibonacci(5)) # 8

num = int(input("Enter a number: "))

print("Reccursion with memoization")
for i in range(0,num):
    print(memo_fibonacci(i))


print("Reccursion without memoization")
for i in range(0,num):
    print(fibonacci(i))
"""