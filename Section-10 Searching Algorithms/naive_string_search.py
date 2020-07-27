"""
Write a function that accepts 2 strings.
Long string and a short string.
If the short string is in the long string then return 
the starting index of the short string in the long string.
Else return -1.
"""

def string_search(long,short):
    if long==short:
        return 0
    if len(long)<len(short):
        return -1

    for i in range(0,len(long)-len(short)+1):
        for j in range(len(short)):
            if long[i+j]!=short[j]:
                break
        else:
            return i
    return -1



print(string_search('hello world','ld'))