"""
# Problem Pattern: Freequency Counter

Problem Statement
-----------------
Given two strings, write a function to determine if the second string is an anagram of the first string.
An anagram is a word, pharase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

1. valid_anagram('','') #True
2. valid_anagram('aaz','aza') #True
3. valid_anagram('anagram','ramgana') #True
2. valid_anagram('qwerty','ytrewq') #True
2. valid_anagram('rat','car') #False
"""

#O(p+q+r) -> O(n)
def fair_enough_valid_anagram(str1, str2): 
    if len(str1)!=len(str2):
        return False

    lookup_table1 = {}
    for char in str1: #O(p)
        if lookup_table1.get(char):
            lookup_table1[char]+=1
        else:
            lookup_table1[char] = 1

    lookup_table2 = {}
    for char in str2: #O(q)
        if lookup_table2.get(char):
            lookup_table2[char]+=1
        else:
            lookup_table2[char] = 1
    
    for key,value in lookup_table2.items(): #O(r)
        if not lookup_table1.get(key):
            return False
        elif lookup_table1[key]!=value:
            return False
        else:
            if lookup_table1.get(key)>0: 
                lookup_table1[key]-=1
            else:
                return False

    if not lookup_table1 or lookup_table2:
        return False

    return True


#O(n+m) -> O(n)
def valid_anagram(str1, str2): #better
    if len(str1) != len(str2):
        return False

    lookup_table = {}
    for char in str1: #O(n)
        if lookup_table.get(char):
            lookup_table[char]+=1
        else:
            lookup_table[char]=1

    for char in str2: #O(m)
        if lookup_table.get(char):
            lookup_table[char]-=1
            if lookup_table[char]==0:
                lookup_table.pop(char)
        else:
            return False

    if lookup_table:
        return False

    return True


print(valid_anagram('','')) #True
print(valid_anagram('aaz','aza')) #True
print(valid_anagram('anagram','ramgana')) #True
print(valid_anagram('qwerty','ytrewq')) #True
print(valid_anagram('rat','car')) #False