/*
# Problem Pattern: Freequency Counter

Problem Statement
-----------------
Given two strings, write a function to determine if the second string is an anagram of the first string.
An anagram is a word, pharase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

Examples:
1. valid_anagram('','') #True
2. valid_anagram('aaz','aza') #True
3. valid_anagram('anagram','ramgana') #True
2. valid_anagram('qwerty','ytrewq') #True
2. valid_anagram('rat','car') #False
*/

function valid_anagram(str1,str2) {
    if (str1.length!=str2.length){
        return false;
    }

    lookup = {};
    for (let char of str1){
        if (lookup.hasOwnProperty(char)){
            lookup[char]+=1;
        }
        else{
            lookup[char]=1;
        }
    }

    for (let char of str2){
        if (lookup.hasOwnProperty(char)){
            lookup[char]-=1;
            if (lookup[char]==0){
                delete lookup.char;
            }
        }
        else{
            return false;
        }
    }
    if (lookup){
        return false;
    }
    return true;
}