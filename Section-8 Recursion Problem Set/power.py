"""
Write a recursive function that takes 2 arguments NUM and POW.
This function should return NUM^POW.

Example:
1. power(5,1) #5
2. power(5,2) #25
3. power(1,16) #1
4. power(5,0) #1
5. power(5,-2) #1/25
"""

#O(n);  n = abs(pow)
def power(num,pow=1):
    if pow==0:
        return 1
    elif pow>0:
        return num*power(num,pow-1)
    else:
        return round(1/num*power(num,pow+1),5)



print(power(5,1) )#5
print(power(5,2) )#25
print(power(1,16)) #1
print(power(5,0) )#1
print(power(1,-996)) #1
print(power(2,-3)) #1/8